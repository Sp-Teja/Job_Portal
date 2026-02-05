from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Job, JobApplication
from .serializers import JobSerializer, JobApplicationSerializer
# Create your views here.


# ---------------------------
# Create Job (Only logged-in users)
# ---------------------------
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_job(request):
    request.data['created_by'] = request.user.id
    serializer = JobSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ---------------------------
# Get All Jobs (with filtering + pagination)
# ---------------------------
@api_view(['GET'])
def list_jobs(request):
    jobs = Job.objects.all()

    # Filtering
    title = request.GET.get("title")
    location = request.GET.get("location")

    if title:
        jobs = jobs.filter(title__icontains=title)
    if location:
        jobs = jobs.filter(location__icontains=location)

    # Simple Pagination (manual)
    page = int(request.GET.get("page", 1))
    limit = 5
    start = (page - 1) * limit
    end = page * limit
    total = jobs.count()

    serializer = JobSerializer(jobs[start:end], many=True)
    return Response({
        "total_jobs": total,
        "page": page,
        "results": serializer.data
    })


# ---------------------------
# Update Job (Only creator)
# ---------------------------
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_job(request, job_id):
    try:
        job = Job.objects.get(id=job_id, created_by=request.user)
    except Job.DoesNotExist:
        return Response({"message": "Job not found or unauthorized"}, status=404)

    serializer = JobSerializer(job, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


# ---------------------------
# Delete Job
# ---------------------------
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_job(request, job_id):
    try:
        job = Job.objects.get(id=job_id, created_by=request.user)
    except Job.DoesNotExist:
        return Response({"message": "Job not found or unauthorized"}, status=404)

    job.delete()
    return Response({"message": "Job deleted successfully"})


# ---------------------------
# Apply for Job
# ---------------------------
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def apply_job(request, job_id):
    data = {
        "job": job_id,
        "applicant": request.user.id,
        "resume": request.data.get("resume")
    }
    serializer = JobApplicationSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors)


def job_list_page(request):
    return render(request, "job_list.html")

def create_job_page(request):
    return render(request, "create_job.html")

def apply_job_page(request):
    return render(request, "apply_job.html")
