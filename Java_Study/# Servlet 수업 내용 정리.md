# Servlet 수업 내용 정리

## 1. Servlet 이란?
- Java 기반의 웹 처리 기술
- 클라이언트 요청(Request)을 받아 처리 후 응답(Response)을 반환
- Tomcat 같은 WAS(Web Application Server)에서 실행됨

---

## 2. URL 매핑

```java
@WebServlet("/Input2")
/Input2 주소 요청 시 해당 Servlet 실행
실행 URL 예시
http://localhost:8080/pro06/Input2
3. GET 방식 요청

URL 뒤에 데이터를 붙여 전달

?user_id=Lee&user_pw=1234
이름=값 형태
여러 데이터는 & 로 연결

예시:

http://localhost:8080/pro06/Input2?user_id=Lee&user_pw=1234
4. request 객체

클라이언트가 보낸 요청 정보를 저장

단일 파라미터 받기
String user_id = request.getParameter("user_id");
5. 여러 값 받기

체크박스처럼 여러 값 선택 시 사용

String[] values = request.getParameterValues("subject");
6. 모든 파라미터 이름 조회
Enumeration<String> enu = request.getParameterNames();
모든 파라미터 이름 순회 가능

예:

user_id
user_pw
subject
7. Enumeration 사용
while (enu.hasMoreElements()) {

    String name = enu.nextElement();

}
hasMoreElements()
다음 요소 존재 여부 확인
nextElement()
다음 요소 반환
8. 콘솔 출력
System.out.println();
Eclipse Console 창에 출력됨
9. 브라우저 출력
PrintWriter out = response.getWriter();
out.println();
브라우저 화면에 출력됨
10. response 객체

서버가 클라이언트에게 응답할 때 사용

response.setContentType("text/html;charset=utf-8");
HTML 형식 응답
UTF-8 한글 처리
11. Servlet 생명주기
init()
public void init()
Servlet 최초 생성 시 1번 실행
doGet()
protected void doGet()
GET 요청 시 실행
destroy()
public void destroy()
서버 종료 시 실행
12. 전체 흐름
HTML 입력
 ↓
GET 요청
 ↓
Servlet 실행
 ↓
request 객체로 데이터 받기
 ↓
처리
 ↓
response 객체로 응답