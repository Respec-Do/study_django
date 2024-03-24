# 학생의 번호, 국어, 영어, 수학 점수를 전달받은 뒤
# 총점과 평균을 화면에 출력한다.
from django.shortcuts import render, redirect
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView


# form태그는 get방식을 사용한다.
# 출력 화면에서 다시 입력화면으로 돌아갈 수 있게 한다.

# 입력: task/student/register.html
# 출력: task/student/result.html

class StudentRegisterFormView(View):
    def get(self, request):
        return render(request, 'task/student/register.html')


class StudentRegisterView(View):
    def get(self, request):
        data = request.GET
        data = {
            'id': data['id'],
            'kor': int(data['kor']),
            'eng': int(data['eng']),
            'math': int(data['math'])
        }

        total = data['kor'] + data['eng'] + data['math']
        average = round(total / 3, 2)

        return redirect(f'/student/result?total={total}&average={average}')


class StudentResultView(View):
    def get(self, request):
        data = request.GET
        context = {
            'total': request.GET['total'],
            'average': request.GET['average']
        }
        return render(request, 'task/student/result.html', context)

# 회원의 이름과 나이를 전달받는다.
# 전달받은 이름과 나이를 아래와 같은 형식으로 변경시킨다.
# "홍길동님은 20살!"
# 결과 화면으로 이동한다.

class MemberRegisterFormView(View):
    def get(self, request):
        return render(request, 'task/member/register.html')

class MemberRegisterView(View):
    def get(self, request):
        data = request.GET
        data = {
            'name' : data['name'],
            'age' : data['age']
        }

        return redirect(f'/member/result?name={data["name"]}&age={data["age"]}')

class MemberResultView(View):
    def get(self, request):
        data = request.GET
        context = {
            'name': request.GET['name'] + '님은',
            'age': request.GET['age'] + '살!'
        }
        return render(request, 'task/member/result.html', context)

# 이름과 나이 작성: task/member/register.html
# 결과 출력: task/member/result.html


# 학생의 이름과 나이 전화번호 입력 : task/student/register2.html
# 결과 출력 : task/student/result2.html

class StudentRegister2FormView(View):
    def get(self, request):
        return render(request, 'task/student/register2.html')

class StudentRegister2View(View):
    def get(self, request):
        data = request.GET
        data = {
            'name' : data['name'],
            'age' : data['age'],
            'number' : data['number']
        }

        return redirect(f'/student/result2?name={data["name"]}&age={data["age"]}&number={data["number"]}')

class StudentResult2View(View):
    def get(self, request):
        data = request.GET
        context = {
            'name': request.GET['name'] + '님은',
            'age': request.GET['age'] + '살!',
            'number' : '번호는' + request.GET['number']
        }
        return render(request, 'task/student/result2.html', context)


# 상품 정보
# 번호, 상품명, 가격, 재고
# 상품 1개 정보를 REST 방식으로 설계한 뒤
# 화면에 출력하기
# 예시)
# product/1
# task/product/product.html

# 순서가 중요하다. urls 부터 만들고 product1부터 만든 다음 html만들기 해야함.

# 상품 정보
# 번호, 상품명, 가격, 재고
# 상품 1개 정보를 REST 방식으로 설계한 뒤
# 화면에 출력하기
# 예시)
# products/1
# task/product/product.html
class ProductDetailView(View):
    def get(self, request):
        return render(request, 'task/product/product.html')


class ProductDetailAPI(APIView):
    def get(self, request, product_id):
        data = {
            'id': product_id,
            'product_name': '마우스',
            'product_price': 50000,
            'product_stock': 50
        }
        return Response(data)

















