# views.py
import requests
from datetime import datetime, timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

GENDERIZE_URL = "https://api.genderize.io"


@api_view(['GET'])
def classify_name(request):
    name = request.GET.get('name')

    # --- Validation ---
    if name is None or name.strip() == "":
        return Response(
            {"status": "error", "message": "Missing or empty name parameter"},
            status=status.HTTP_400_BAD_REQUEST
        )

    if not isinstance(name, str):
        return Response(
            {"status": "error", "message": "name must be a string"},
            status=status.HTTP_422_UNPROCESSABLE_ENTITY
        )

    try:
        # --- External API Call ---
        response = requests.get(GENDERIZE_URL, params={"name": name}, timeout=2)

        if response.status_code != 200:
            return Response(
                {"status": "error", "message": "Upstream service error"},
                status=status.HTTP_502_BAD_GATEWAY
            )

        data = response.json()

        gender = data.get("gender")
        probability = data.get("probability")
        count = data.get("count")

        # --- Edge Case Handling ---
        if gender is None or count == 0:
            return Response(
                {
                    "status": "error",
                    "message": "No prediction available for the provided name"
                },
                status=status.HTTP_422_UNPROCESSABLE_ENTITY
            )

        # --- Processing ---
        sample_size = count
        is_confident = probability >= 0.7 and sample_size >= 100

        processed_at = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

        return Response(
            {
                "status": "success",
                "data": {
                    "name": name.lower(),
                    "gender": gender,
                    "probability": probability,
                    "sample_size": sample_size,
                    "is_confident": is_confident,
                    "processed_at": processed_at
                }
            },
            status=status.HTTP_200_OK
        )

    except requests.exceptions.RequestException:
        return Response(
            {"status": "error", "message": "Failed to reach upstream service"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )