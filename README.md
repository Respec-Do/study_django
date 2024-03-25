# **Framework**

- 라이브러리  
  > 개발자가 작성해놓은 코드 파일을 의미한다.
- API  
  > 여러 라이브러리가 모여있는 압축파일을 의미한다.
- Framework  
  > API가 굉장히 많이 모여져서 덩치가 커져있는 것을 의미한다.

## Framework 장점

-   개발에 필요한 구조를 이미 코드로 만들어 놓았기 때문에,  
    실력이 부족한 개발자라 하더라도
    반쯤 완성된 상태에서 필요한 부분을 조립하는 형태의 개발이 가능하다.
-   회사 입장에서는 Framework를 사용하면 일정한 품질이 보장되는 결과물을 얻을 수 있고,  
    개발자 입장에서는 완성된 구조에 자신이 맡은 서비스에 대한 코드를 개발해서 넣기 때문에
    개발 시간을 단축할 수 있다.
    <br>
    <br>

## Django Framework

-   파이썬으로 만들어진 오픈 소스 웹 애플리케이션 프레임워크이며,  
    빠르고 쉽게 웹 사이트를 개발할 수 있는 구성 요소로 이루어진 웹 프레임워크이다.

## Django Framework의 특징

0. **Table -> Model -> View -> Template**

1. **★★MVT 소프트웨어 디자인 설계 패턴★★**

-   Model : 테이블에 저장되어 있는 데이터를 불러온 뒤 담아놓는 역할 (Model 객체)
-   View : 테이블에 접근한 뒤 화면에서 사용할 Model객체를 완성시킨다.
-   Templates : 클라이언트에게 보여질 화면 구성, 전달받은 Model객체를 사용한다.

2. **강력한 ORM**

-   ORM(Object Relational Mapping)은 **객체 관계 매핑**이며,
-   객체 진영과 RDB 진영의 구조 차이를 자동으로 해결해주는 기술의 총칭이다.
-   오로지 객체를 중심으로 설계가 가능하며, 직접 SQL문을 작성하지 않아도 자동으로 쿼리가 생성되어 실행된다.

3. **자체 템플릿 지원**

-   HTML에서 연산이 가능하도록 도와주며, 자체 템플릿 태그가 있기 때문에 동적인 페이지를 구성할 수 있게 해준다.

4. **소스코드 변경 감지**

-   .py 파일의 소스코드가 변경된다면, 이를 자동으로 감지하여 서버를 재시작해준다.

5. **WAS에 종속적이지 않은 환경**

-   WAS : Web Applicatoin Server
-   서버를 실행하지 않아도 기능별 단위 테스트가 가능하기 때문에 버그를 줄이고 개발 시간을 단축할 수 있다.

## Django Framework의 장점

1. 확장성

-   객체를 기억하여 재사용할 수 있는 캐싱과 코드 재사용 기능으로 인해 확장성이 좋다.

2. 보안

-   개발자가 SQL 주입, CSRF 공격 및 XSS와 같은 많은 보안 문제를 피할 수 있도록 도와준다.

3. 기본 라이브러리를 통한 빠른 개발

-   처음부터 코드를 작성하는 대신 여러 기능을 포함하는 패키지를 활용할 수 있다.

## Django Framework의 목적

-   간단한 웹 앱을 제작하거나 Python을 필요로 하는 서비스들을 가볍게 제작하여,  
    MSA (\*마이크로 서비스)로 나누어 개발하는 목적으로 사용된다.

<br>
<hr>

# Model 

-   Django에서 models.Model 이라는 추상화된 클래스를 사용하여 데이터베이스에 테이블을 정의할 수 있다.
-   models.Model 을 상속받은 클래스로 구현할 수 있으며, 내부 클래스로 Meta 클래스를 선언할 수 있다.

## Model Convention

-   모델 내 코드를 작성할 때 아래의 순서에 맞춰 작성하는 것을 권장한다.

    1. Constant for choices
    2. All databases Field
    3. Custom manager attributes
    4. class Meta
    5. def \_\_str\_\_()
    6. def save()
    7. def get_absolute_url()
    8. Any custom methods

### 1. Constant for choices

-   DB에 저장할 값과 실제 화면에 보여지는 값이 다를 경우 미리 튜플 형태로 선언해 놓고 사용한다.

          Constant = [
                      ('DB 저장 값', '화면 출력 값'),
                      ...
                  ]

### 2. All databases Field

-   ForeignKey(to, verbose_name, related_name, related_query_name, on_delete, null)
-   OneToOneField(to, verbose_name, related_name, related_query_name, on_delete, null)
-   ManyToManyField((to, verbose_name, related_name, related_query_name, on_delete, null))
    <br>

-   related_name
    > 역참조가 필요한 다대다 또는 일대다 관계에서 유용하게 사용된다.  
    > B필드에 a객체 선언 후 참조 시 b.a로 접근할 수 있으나  
    > 역참조인 a.b로는 접근할 수 없다. A필드에는 b객체가 없기 때문이다.  
    > _set객체를 사용하면 역참조가 가능하고 a.b_set으로 역참조가 가능하다.  
    > 만약 _set객체의 이름을 다른 이름으로 사용하고자 할 떄 바로 related_name을 사용한다.
    <br>
    <br>

ⓐ **문자열**
   - 문자열 필드는 null=False로 하고 필수 요소가 아니라면 blank=True로 설정한다.  
   - 이렇게 설정하는 이유는 null과 빈 값을 "null이거나 빈 문자일 경우 빈 값이다" 라고 검사할 필요없이  
     빈 문자열인지로만 판단할 수 있게 되기 때문이다.

         최대 길이 제한이 필요한 경우
         - CharField(verbose_name, max_length, choices, unique, blank, null, default)

         최대 길이 제한이 필요 없는 경우
         - TextField(verbose_name, null=False, blank=True)

ⓑ **정수**
  - PositiveSmallIntegerField(verbose_name, choices, null, default)  
  - SmallIntegerField(verbose_name, choices, null, default)  
  - IntegerField(verbose_name, choices, null, default): 4byte  
  - BigIntegerField(verbose_name, choices, null, default)  
  - BooleanField(verbose_name, default): 1byte

ⓒ **날짜**
  - auto_now_add=True
    > 최초 한 번만 자동으로 필드 값을 현재 시간으로 설정한다.
    > 보통 등록 날짜 항목으로 사용된다.

  - auto_now=True
    > 객체가 변경될 때마다 자동으로 필드 값을 현재 시간으로 수정한다.  
    > 보통 수정된 날짜 항목으로 사용된다.  
    > 하지만, save()를 사용해야 적용되고 update()를 사용하면 적용되지 않는다.  
    > auto_now=True처럼 사용하고 싶다면, default=timezone.now를 사용하는 것이 올바르다.  
    > ※ django.utils.timezone.now으로 설정한 뒤 update할 때 마다 그 때의 now로 넣어준다.

- DateField(verbose_name, null, default, auto_now_add)
- TimeField(verbose_name, null, default, auto_now_add)
- DateTimeField(verbose_name, null, default, auto_now_add)

### 3. Custom manager attributes

-   데이터베이스와 상호작용하는 인터페이스(틀)이며, Model.objects 속성을 통해 사용한다.  
-   Custon manager와 Custom QuerySet을 통해 사용할 수 있으며,  
    공통적으로 사용되는 쿼리를 공통함수로 정의할 수 있고 실제 동작을 숨길 수 있다.

### 4. Class Meta

-   Model 클래스 안에 선언되는 내부 클래스이며, 모델에 대한 기본 설정들을 변경할 수 있다.  
-   Meta 클래스가 작동하기 위해서는 정해진 속성과 속성 값을 작성해야 하고,  
    이를 통해 Django를 훨씬 편하게 사용할 수 있다.

        데이터 조회 시 정렬 방법 설정
            1. 오름차순
                ordering = ['필드명']
            2. 내림차순
                ordering = ['-필드명']

        테이블 생성 시 이름 설정
            db_table =  '테이블명'

        테이블을 생성할 것인 지 설정
            abstract = False

### 5. def \_\_str\_\_()

-   객체 조회 시 원하는 데이터를 직접 눈으로 확인하고자 할 때 사용하며, 객체 출력 시 자동으로 사용되는 메소드이다.
-   모델 필드 내에서 재정의하여 원하는 필드를 문자열로 리턴하면 앞으로 객체 출력 시 해당 값이 출력된다.

### 6. def save()

-   모델 클래스를 객체화한 뒤 save()를 사용하면 INSERT 또는 UPDATE 쿼리가 발생한다.  
    이는 Django ORM이 save()를 구현해놨기 때문이다.  
-   save() 사용 시, INSERT 또는 UPDATE 쿼리 발생 외 다른 로직이 필요할 경우 재정의할 수 있다.  
    하지만 재정의를 하면, 객체를 대량으로 생성하거나 수정할 때 동작하지 않는다.

### 7. def get_absolute_url()

-   모델에 대해서 상세보기(DetailView)를 제작한다면, redirect(모델 객체)를 통해 자동으로 get_absolute_url()을 호출한다.
-   추가 혹은 수정 서비스 이후 상세보기 페이지로 이동하게 된다면,
    매번 redirect에 경로를 작성하지 않고 get_absolute_url()을 재정의해서 사용하는 것을 추천한다.

### 8. Any Custom methods
<hr>

# CRUD_QuerySet 

    일반적으로 기존 객체에 자주 영향을 미치는 메소드는 자신(self)을 리턴하지 않도록 하는 것이
    Python에서 좋은 사례로 간주된다. 만약 객체로 접근한 메소드가 자신(self)를 리턴하게 되면
    계속 이어서 코드를 작성하게 되고(메소드 체인), 이 때 특정 버그나 문제가 발생했을 때 
    찾기 힘들 뿐더러 전체 기능에 문제가 생길 수 있다.

## 생성(CREATE)

    1. craete()
    
          모델명.objects.create()
          전달한 값으로 초기화한 뒤 새로운 객체를 생성하고 테이블에 저장한다.

    2. save()
    
          객체명.save()
          전달한 값으로 태아블에 저장된다.

    3. bulk_create()
    
          모델명.objects.bulk_create([])
          전달한 list로 초기화 된 여러 개의 객체를 생성하고 테이블에 저장한다.
          생성된 객체들은 list 타입을 리턴된다.

    4. get_or_create()
    
          obj, isCreated = 모델명.objects.get_or_create()
          테이블에 객체가 있으면 가져오고, 없으면 테이블에 저장되고 만들어진 객체를 리턴한다.
          추가 정보는 defaults={}로 전달해서 create일 경우 사용된다.
          두 칸짜리 tuple 타입으로 리턴되며, 첫번째는 객체, 두번째는 생성여부인 bool타입이 담긴다.

## 조회(SELECT)

    1. get()
    
          모델명.objects.get()
          테이블에서 조건에 맞는 한개의 객체를 조회한다.
          조회된 값이 없으면 DoseNotExitst, 2개 이상이면
          MultipleObjectsReturned가 발생하기 때문에 조회할 값이 1개일 때만 사용한다.

    2. all()
          
          모델명.objects.all()
          테이블에서 전체 정보를 조회한다.
          QuerySet 객체를 리턴하며, 조회된 객체들이 들어있다.
          QuerySet이란, 쿼리의 결과를 전달받은 모델 객체 목록이다.
          list와 구조는 같지만, 파이썬 기본 자료구조가 아니기 때문에 형변환이나 serializer(직렬화)가 필요하다.

    3. values()
    
          테이블에서 전체 정보를 조회한다.
          QuerySet 객체를 리턴하며, 조회된 객체가 dict 타입으로 들어있다.
          필드 이름을 전달하면 원하는 필드 정보만 가져올 수 있다.
          참조 중인 테이블의 필드를 가져오기 위해서는 '[참조중인 객체명]__[필드명]' 으로 작성한다.

    4. values_list()
    
          테이블에서 전체 정보를 조회한다.
          QuerySet 객체를 리턴하며 조회된 객체가 tuple 타입으로 들어있다.
          모든 필드를 순서대로 가져오고 싶을 때 인덱스로 접근해서 가져올 수 있다.

    5. filter()
    
          조건에 맞는 행을 조회한다.
          QuerySet 객체를 리턴하며, 조회된 객체들이 들어있다.
          조건에 맞는 결과가 한 개도 없을 경우 비어있는 QuerySet이 리턴된다.

    6. exists()
     
          filter()와 함께 사용해서 filter 조건에 맞는 데이터가 있는 지 조회한다.

    7. exclude()
    
          조건에 맞지 않는 행을 조회한다.
          QuerySet 객체를 리턴하며, 조회된 객체들이 들어있다.
          조건에 맞는 결과가 한 개도 없을 경우 비어있는 QuerySet이 리턴된다.

    8. AND, OR
    
        AND - 모델명.objects.filter() & 모델명.objects.filter()
        OR - 모델명.objects.filter() | 모델명.objects.filter()

        AND - 모델명.objects.filter(key=value, key=value)
        OR - 모델명.objects.filter(Q(key=value) | Q(key=value))

    9. first(), last()
    
          모델명.objects.filter().first()
          조건에 맞는 QuerySet 결과 중 첫 번째 객체만 가져오기

          모델명.objects.filter().last()
          조건에 맞는 QuerySet 결과 중 마지막 객체만 가져오기

    10. count()
    
          모델명.objects.filter().count()
          조건에 맞는 결과의 총 개수를 리턴한다.

    11. order_by()
          
          모델명.object.order_by('필드명') : 오름차순
          모델명.object.order_by('-필드명') : 내림차순

    12. annotate()
    
          모델명.objects.annotate().values()
          모델명.objects.values().annotate()
          결과 테이블에서 컬럼을 다른 이름으로 사용하거나 다른 연산을 수행한 뒤 새로운 이름을 만들어낸다.

    13. aggregate()
    
          QuerySet객체.aggregate(key=집계함수('필드명'))
          QuerySet객체.values("묶을 필드명").annotate(key=집계함수('필드명'))
          각 전체 대상과 그룹 대상이다.

## 수정(UPDATE)

        1. save()
        
            존재하는 개체를 조회한 뒤 전체 필드를 수정하고 혹시 없는 객체라면 추가한다.
            수정 목적의 글로 사용할 때에는 어떤 필드가 수정되었는 지를 정확히 알려주어야 한다.
            Ex) save(update_field=['',...])

        2. update()
            
            QuerySet객체로 사용하 수 있으며, 해당 개게들을 수정하고 수정된 행의 수를 리턴한다.

## 삭제(DELETE)

    1. delete()
        
        객체.delete()로 사용하여 조건에 맞는 모든 행을 삭제한다.
        get(), filter(), all()과 같이 사용한다.

<hr>

# REST 

    Representational State Transfer (데이터를 응답하는 방식)

    언제 어디서든 누구든 서버에 요청을 보낼 때,
    URI만으로도 데이터 또는 행위 (CRUD) 상태를 이해할 수 있도록 설계하는 규칙

    DRF (Django Rest Framework)

-   작성방법

1. 소문자로 작성한다.

    - 대문자로 작성 시 문제가 발생할 수 있기 때문에 소문자로 작성한다

2. 언더바 대신 하이픈을 사용한다.

    - 가독성을 높이기 위해서 하이픈으로 구분하는 것이 좋다.

3. URI 마지막에 슬래시를 작성하지 않는다.

    - 마지막에 작성하는 슬래시는 의미가 없다.

4. 계층 관계 표현 시 슬래시 구분자로 사용한다.

    - 계층 관계(포함 관계)에서는 슬래시로 구분한다.

5. 파일 확장자는 포함시키지 않는다.

    - 파일 확장자는 URI로 표현하지 않고 Header의 Content-Type을 사용하여
      body의 내용을 처리하도록 설계한다.

6. 데이터를 대표할 때에는 명사를 사용하고, 상태를 대표할 때에는 동사를 사용한다.

    - https://www.app.com/members/get/1 (X)
    - https://www.app.com/members/delete/1 (O)

7. URI에 사용되는 영어 단어는 복수로 작성한다.

<hr>
<br>

# Command 명령어

        가상환경으로 접속
            venv/Scripts/activate

        현재 설치된 라이브러리를 파일로 정리
            pip freeze > requirements.txt

        새로운 서비스 폴더 만들기
            python manage.py startapp [서비스 이름]

        requirements.txt에 작성된 라이브러리 설치
            pip install -r requirements.txt

        ※ 최초 1회에만 사용
        Model 객체 및 settings.py 설정 반영 파일 제작
            python manage.py makemigrations [서비스 이름]

        ※ 최초 1회에만 사용
        makemigrations로 만든 migration 파일 실행
            python manage.py migrate [서비스 이름]

        ※ migration 전체 삭제
            python manage.py migrate --fake [서비스 이름] zero

        직접 migrations 파일 삭제!!
        직접 DBMS 테이블 DROP !!

## 서버 실행

-   python manage.py runserver [포트 번호]

<hr>

# View에 대하여

- 왜 직접 타지 않고 서버를 거쳐서 가는가?
  1. 실제 경로를 숨기기 위해, 보안의 목적성
  2. DB의 조회등 연산의 목적성

- 요청 과정

      a.html -> urls.py -> views.py -> b.html

- Example)

      수정 : Post/update
             Post/update-ok
      --> 두 개의 경로가 필요
          1개의 경로만 사용하자!

      Post/update의 요청방식
      Get / Post

## 요청 방식
- GET
- POST

### GET
  - 수정할 데이터를 가져올 때
    > ex) id=3
  - url에 담아서 가는 방식 
    > ex) a/b ? name=홍길동
  - 길이의 제한이 있고 숨겨야하는 데이터에는 GET을 사용하면 안됨.
  - POST 방식보다 GET이 빠름.
 
### POST
  - 수정완료를 눌렀을 때
  - 길이의 제한이 없음 (숨겨져 있음)
  - url에 보이지 않음
  - 요청할 때 header에 request header라는 이름으로 key:value로 저장해서 전달함.

## 응답 방식
- render
- redirect

### render
- 화면에서 화면으로 데이터를 보낼 수 있다.

### redirect
- view로 가기 때문에 데이터를 담아서 보낼 수 없다.

### 왜 굳이 REDIRECT를 이용해야하는가?
- RENDER 는 요청한 경로가 표시가 된다.
- 만일, 결제 정보에서 render로 보내게 되면, 기존 정보가 다 담겨있어서 새로고침하게 되면 계속 결제가 되는 문제가 발생한다.
  > Ex) pay/write로 계속 표기가 됨.
- REDIRECT 는 초기화가 된다.
  > Ex) redirect로 보내게 되면, 기존 정보들이 초기화되면서, 새로고침해도 pay/success로 표기가 된다.

# 24.02.28 트러블 슈팅

        게시글 목록
        
        문제발생
            게시글 조회 -> 알맞은 페이지의 데이터 조회 [offset:limit]
            redner()를 통해서 화면에 전달하려고 했으니
            화면에서 객체를 제대로 쓸 수 없었다.
        트러블 슈팅
            REST라는 규칙을 배운 뒤 게시글 목록 데이터를 직렬화 했다.
            APIView를 상속받은 뒤 Response()객체에 원하는 데이터를
            데이터를 전달해서 리턴했다. 데이터를 응답하는 것 까지 확인했다.

        화면에서 REST 방식의 API를 사용할 때 비동기 통신이 필요했다.
        XMLHttpRequest, Ajax, Axios, fetch 등 Javascript로
        통신할 수 있는 방법은 다양하지만, 가장 간단한 fetch를 선택했다.
        fetch()에 원하는 요청 경로를 작성하고, 이를 통해 얻은 결과 데이터를
        알맞게 화면에 출력한다.

        
