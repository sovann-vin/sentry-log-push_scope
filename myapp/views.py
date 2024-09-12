import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import uuid
from vine import Thenable
from sentry_sdk import (
    capture_message,
    push_scope,
    configure_scope,
    isolation_scope,
    new_scope,
    capture_exception
)

class TestAPIView(APIView):
    def get(self, request):
        try:
            # for _ in range(5):
            #     unique_id = str(uuid.uuid4())
            #     print("unique_id", unique_id)

            object = {
                "name": "John Doe",
                "age": 25,
                "email": "h@gmail.com"  
            }
            with new_scope() as scope:
                scope.set_context('request data', object)
                capture_message('testing the object', level='error')

            # test = [
            #         '14991',
            #         '14992',
            #         '14993',
            #         '14994',
            #         '14995'
            #     ]
            # for unique_id in test:
            #     print("unique_id", unique_id)
            #     with sentry_sdk.isolation_scope() as scope:
            #             scope.set_tag('unique_id', unique_id)
            #             scope.set_context('request data', {"isolation_scope":"value 1", "isolation_scope":"value 2"})
            #               # Add more tags as needed
                        
            #             # Capture the message with a unique fingerprint
            #             sentry_sdk.capture_message(
            #                 'pushh scope validation error ' + unique_id, 
            #                 level='error',
            #                 fingerprint=[unique_id]
            #             )
            return Response({"message": "This is a test API endpoint"}, status=status.HTTP_200_OK)
        except Exception as e:
            # Log the exception to Sentry or handle it as needed
            capture_exception(e)
            
            # Return a response indicating an error occurred
            return Response({
                "error": "An error occurred while processing your request."
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
