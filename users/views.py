from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import make_password
from .models import User

@api_view(['POST'])
def login_user(request):
    email = request.data.get('email')
    password = request.data.get('password')

    if not email or not password:
        return Response({'error': 'Please provide both email and password'}, 
                      status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(email=email, password=password)

    if user:
        refresh = RefreshToken.for_user(user)
        return Response({
            'token': str(refresh.access_token),
            'user': {
                'email': user.email,
                'username': user.username
            }
        })
    else:
        return Response({'error': 'Invalid credentials'}, 
                      status=status.HTTP_401_UNAUTHORIZED)

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import UserSurvey
from .serializers import UserSurveySerializer

@api_view(['POST'])
def submit_survey(request):
    try:
        serializer = UserSurveySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Survey submitted successfully',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({
            'error': str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_states(request):
    states = [
        'Andhra Pradesh', 'Bihar', 'Chhattisgarh', 'Delhi', 'Gujarat', 'Haryana',
        'Himachal Pradesh', 'Jharkhand', 'Karnataka', 'Kerala', 'Madhya Pradesh',
        'Maharashtra', 'Odisha', 'Punjab', 'Rajasthan', 'Tamil Nadu', 'Telangana',
        'Uttar Pradesh', 'West Bengal'
    ]
    return Response(states)

@api_view(['GET'])
def home_stats(request):
    # Get total submissions
    total_submissions = UserSurvey.objects.count()
    
    # Get unique states count
    states_covered = UserSurvey.objects.values('state').distinct().count()
    
    # Calculate unemployment rate
    total_users = UserSurvey.objects.count()
    unemployed = UserSurvey.objects.filter(status='Unemployed').count()
    unemployment_rate = (unemployed / total_users * 100) if total_users > 0 else 0
    
    return Response({
        'total_submissions': total_submissions,
        'states_covered': states_covered,
        'unemployment_rate': round(unemployment_rate, 2)
    })

@api_view(['GET'])
def dashboard_data(request):
    # Get total submissions
    total_submissions = UserSurvey.objects.count()
    
    # Get state-wise data
    state_data = UserSurvey.objects.values('state').annotate(count=Count('state'))
    
    # Get employment status data
    employment_data = UserSurvey.objects.values('status').annotate(count=Count('status'))
    
    # Get education-wise data
    education_data = UserSurvey.objects.values('education').annotate(count=Count('education'))
    
    # Get job type distribution
    job_type_data = UserSurvey.objects.values('jobtype').annotate(count=Count('jobtype'))
    
    # Calculate unemployment rate
    total_users = UserSurvey.objects.count()
    unemployed = UserSurvey.objects.filter(status='Unemployed').count()
    unemployment_rate = (unemployed / total_users * 100) if total_users > 0 else 0
    
    return Response({
        'total_submissions': total_submissions,
        'state_data': state_data,
        'employment_data': employment_data,
        'education_data': education_data,
        'job_type_data': job_type_data,
        'unemployment_rate': round(unemployment_rate, 2)
    })


@api_view(['POST'])
def register_user(request):
    try:
        data = request.data
        
        # Check if email already exists
        if User.objects.filter(email=data['email']).exists():
            return Response({'error': 'Email already registered'}, 
                          status=status.HTTP_400_BAD_REQUEST)

        # Create new user
        user = User.objects.create(
            username=data['email'],  # Using email as username
            email=data['email'],
            password=make_password(data['password']),
            first_name=data['firstName'],
            last_name=data['lastName']
        )

        # Create user profile with additional details
        user.profile.date_of_birth = data['dateOfBirth']
        user.profile.education = data['education']
        user.profile.save()

        return Response({
            'message': 'Registration successful',
            'user': {
                'email': user.email,
                'name': f"{user.first_name} {user.last_name}"
            }
        }, status=status.HTTP_201_CREATED)

    except Exception as e:
        return Response({'error': str(e)}, 
                      status=status.HTTP_500_INTERNAL_SERVER_ERROR)


from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def about_data(request):
    return Response({
        'mission': {
            'title': 'Our Mission',
            'description': 'To track and analyze youth unemployment trends across India, providing valuable insights for policymakers and organizations.'
        },
        'stats': {
            'users_registered': User.objects.count(),
            'states_covered': UserSurvey.objects.values('state').distinct().count(),
            'total_surveys': UserSurvey.objects.count()
        },
        'team': [
            {
                'name': 'Rohit Kumar',
                'role': 'Project Lead',
                'description': 'Expert in data analysis and youth employment trends'
            },
            {
                'name': 'Priya Singh',
                'role': 'Research Analyst',
                'description': 'Specializes in employment policy research'
            },
            {
                'name': 'Amit Patel',
                'role': 'Data Scientist',
                'description': 'Focuses on predictive modeling of employment trends'
            }
        ]
    })


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .models import Survey
from .serializers import SurveySerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def submit_survey(request):
    serializer = SurveySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_survey_stats(request):
    total_surveys = Survey.objects.count()
    employment_stats = Survey.objects.values('employment_status').annotate(count=Count('id'))
    education_stats = Survey.objects.values('education').annotate(count=Count('id'))
    state_stats = Survey.objects.values('state').annotate(count=Count('id'))
    
    return Response({
        'total_surveys': total_surveys,
        'employment_stats': employment_stats,
        'education_stats': education_stats,
        'state_stats': state_stats
    })

@api_view(['POST'])
def submit_contact(request):
    try:
        name = request.data.get('name')
        email = request.data.get('email')
        subject = request.data.get('subject')
        message = request.data.get('message')

        # Basic validation
        if not all([name, email, subject, message]):
            return Response({
                'error': 'All fields are required'
            }, status=status.HTTP_400_BAD_REQUEST)

        # Send email notification
        email_subject = f'Contact Form: {subject}'
        email_message = f'From: {name}\nEmail: {email}\n\nMessage:\n{message}'
        
        send_mail(
            email_subject,
            email_message,
            settings.DEFAULT_FROM_EMAIL,
            [settings.CONTACT_EMAIL],
            fail_silently=False,
        )

        return Response({
            'message': 'Your message has been sent successfully!'
        }, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({
            'error': str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)