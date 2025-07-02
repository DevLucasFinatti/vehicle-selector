from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from cs2test.app.models.responses import Response as ApiResponse

@api_view(['POST'])
def test(request: Request):
    
    return ApiResponse.SuccessResponse(
        success=True, 
        status_code=200, 
        data="Teste foi um sucesso"
    ).to_drf_response()