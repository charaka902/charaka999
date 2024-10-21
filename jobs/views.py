from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # Ensure you have a home.html template

class JobSearchView(APIView):
    def post(self, request):
        title = request.data.get("title")
        location = request.data.get("location")

        response_data = {
            "searchParams": {
                "title": {
                    "id": "dummy_id",
                    "name": title
                },
                "area": {
                    "id": "dummy_area_id",
                    "level": "MSA",
                    "name": location
                },
                "occupations": [],
                "skills": []
            },
            "data": {
                "supply": {
                    "benchmarkIndex": 3.5,
                    "profiles": 99301,
                    "companies": 10388,
                    "supplyRating": "Very Strong Supply"
                },
                "demand": {
                    "benchmarkIndex": 2.2,
                    "postings": 72922,
                    "companies": 4515,
                    "demandRating": "Very High Demand"
                },
                "compensation": {
                    "benchmarkIndex": 1.3,
                    "minSalary": 60575,
                    "medianSalary": 141453,
                    "maxSalary": 244870,
                    "medianAdvertisedSalary": 107776,
                    "wageRating": "Somewhat High Wage Inflation"
                },
                "diversity": {
                    "regional": 54355,
                    "regionalPct": 0.5814,
                    "national": 728217,
                    "nationalPct": 0.4725
                }
            }
        }

        return Response(response_data, status=status.HTTP_200_OK)


class JobSearchDetailedView(APIView):
    def post(self, request):
        title = request.data.get("title")
        city = request.data.get("city")

        response_data = {
            "searchParams": {
                "title": {
                    "id": "ET6850661D6AE5FA86",
                    "name": title
                },
                "area": {
                    "id": "42660",
                    "level": "MSA",
                    "name": "Seattle-Tacoma-Bellevue, WA"
                },
                "occupations": [
                    {
                        "id": "15-1252",
                        "name": "Software Developers"
                    }
                ],
                "skills": []
            },
            "data": {
                "summary": {
                    "benchmarkIndex": 3.5,
                    "profiles": 99301,
                    "companies": 10388,
                    "supplyRating": "Very Strong Supply"
                },
                "companies": [
                    {"id": "8046280", "name": "Microsoft", "profiles": 22592},
                    {"id": "20", "name": "Amazon", "profiles": 13666},
                    # Add more companies here...
                ],
                "skills": [
                    {"id": "KS440QS66YCBN23Y8K25", "name": "Software Engineering", "profiles": 60622},
                    {"id": "KS120L96KMYTDJ48NRSH", "name": "Software Development", "profiles": 54693},
                    # Add more skills here...
                ],
                "titles": [
                    {"id": "ET6850661D6AE5FA86", "name": "Software Engineers", "profiles": 41437},
                    {"id": "ETC6F5E57496B18612", "name": "Software Development Engineers", "profiles": 15206},
                    # Add more titles here...
                ]
            }
        }

        return Response(response_data, status=status.HTTP_200_OK)

class JobSearchBySkillView(APIView):
    def post(self, request):
        skill_id = request.query_params.get("skill_id")

        # Dummy response data - replace this with actual database query if needed
        response_data = {
            "searchParams": {
                "skill_id": skill_id,
                "skills": [{"id": skill_id, "name": "Python (Programming Language)"}]
            },
            "data": {
                "summary": {
                    "benchmarkIndex": 1.8,
                    "postings": 8500,
                    "companies": 250,
                    "demandRating": "High Demand"
                },
                "companies": [
                    {"id": "1", "name": "Google", "postings": 1200},
                    {"id": "2", "name": "Facebook", "postings": 800}
                ],
                "skills": [
                    {"id": "KS125LS6N7WP4S6SFTCK", "name": "Python", "postings": 5000}
                ]
            }
        }

        return Response(response_data, status=status.HTTP_200_OK)

class JobSearchByTitleView(APIView):
    def post(self, request):
        title = request.data.get("title")
        city = request.data.get("city")  # Updated from area_name to city

        response_data = {
            "searchParams": {
                "title": {
                    "id": "ET6850661D6AE5FA86",  # Example ID
                    "name": title
                },
                "area": {
                    "id": "42660",  # Example area ID
                    "level": "MSA",  # You can update this as necessary
                    "name": city  # Now using the city variable
                },
                "occupations": [
                    {
                        "id": "15-1252",
                        "name": "Software Developers"
                    }
                ],
                "skills": []
            },
            "data": {
                "summary": {
                    "benchmarkIndex": 1.3,
                    "minSalary": 60575,
                    "medianSalary": 141453,
                    "maxSalary": 244870,
                    "medianAdvertisedSalary": 107776,
                    "wageRating": "Somewhat High Wage Inflation"
                },
                "percentiles": [
                    {
                        "percentile": 10,
                        "regional": 88655,
                        "national": 65208
                    },
                    {
                        "percentile": 25,
                        "regional": 115760,
                        "national": 84011
                    },
                    {
                        "percentile": 50,
                        "regional": 141453,
                        "national": 110136
                    },
                    {
                        "percentile": 75,
                        "regional": 162719,
                        "national": 140462
                    },
                    {
                        "percentile": 90,
                        "regional": 190183,
                        "national": 170102
                    }
                ]
            }
        }

        return Response(response_data, status=status.HTTP_200_OK)
