from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny, IsAuthenticated  # 导入权限类
from rest_framework.generics import CreateAPIView, ListAPIView
from django.contrib.auth import authenticate
from django.http import JsonResponse
from .models import Detection, ImageBlog
from .serializers import ImageBlogSerializer

# JWT 用户登录视图
class JWTLoginView(APIView):
    """
    用户登录视图，验证用户名和密码，返回 JWT Token。
    """
    permission_classes = [AllowAny]  # 允许任何用户访问，不需要认证

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        # 验证用户名和密码
        user = authenticate(username=username, password=password)
        if user:
            # 生成 JWT Token
            refresh = RefreshToken.for_user(user)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


# 检测数据上传视图
class DetectionUploadView(APIView):
    """
    接收 Edge System 上传的检测数据和图像
    """
    parser_classes = (MultiPartParser, JSONParser)
    permission_classes = [IsAuthenticated]  # 需要认证用户

    def post(self, request, *args, **kwargs):
        # 获取图像文件
        image = request.FILES.get('image')
        # 获取检测结果
        results = request.data.get('detection_results')

        if not image or not results:
            return Response({"error": "Image and detection results are required."}, status=status.HTTP_400_BAD_REQUEST)

        # 保存到数据库
        detection = Detection.objects.create(image=image, results=results)

        return Response({
            "status": "success",
            "id": detection.id,
            "image_url": detection.image.url
        }, status=status.HTTP_201_CREATED)


# 检测数据列表视图
class DetectionListView(APIView):
    """
    返回存储的检测结果和图像列表
    """
    permission_classes = [IsAuthenticated]  # 需要认证用户

    def get(self, request, *args, **kwargs):
        detections = Detection.objects.all().order_by('-detected_at')
        data = [
            {
                "id": detection.id,
                "image_url": request.build_absolute_uri(detection.image.url),
                "results": detection.results,
                "detected_at": detection.detected_at
            }
            for detection in detections
        ]
        return JsonResponse(data, safe=False, status=status.HTTP_200_OK)


# 图像博客上传视图
class ImageBlogCreateView(CreateAPIView):
    """
    上传图像的视图
    """
    queryset = ImageBlog.objects.all()
    serializer_class = ImageBlogSerializer
    permission_classes = [IsAuthenticated]  # 需要认证用户

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # 保存上传用户


# 图像博客列表视图
class ImageBlogListView(ListAPIView):
    """
    获取图像列表的视图
    """
    queryset = ImageBlog.objects.all().order_by('-created_at')
    serializer_class = ImageBlogSerializer
    permission_classes = [IsAuthenticated]  # 需要认证用户
