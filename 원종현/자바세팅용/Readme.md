# 백준&SWEA vscode 자바세팅
## 1. java se 11 설치
- jdk-11.0.21 설치
## 2. vscode에서 Extension Pack for Java 플러그인 설치
## 3. file -> preferences -> setteings 에서 검색창에 java.home 검색
## 4. (Edit in settings.json) 클릭
- "java.jdt.ls.java.home": "C:\\Program Files\\Java\\jdk-11",    기입
- https://spongeb0b.tistory.com/369 참고

# 백준&SWEA input/output 세팅
- launch.json을 하단과 같이 설정
- 이후, run 등 기본 터미널은 git bash 이용
```
{
    // IntelliSense를 사용하여 가능한 특성에 대해 알아보세요.
    // 기존 특성에 대한 설명을 보려면 가리킵니다.
    // 자세한 내용을 보려면 https://go.microsoft.com/fwlink/?linkid=830387을(를) 방문하세요.
    "version": "0.2.0",
    "configurations": [
        {
            "type": "java",
            "name": "Current File",
            "request": "launch",
            "mainClass": "${file}"
        },
        {
            "type": "java",
            "name": "Main",
            "request": "launch",
            "mainClass": "for_java.Main",
            "projectName": "Algo_c7eb0ae5",
            "args":["<", "for_java/input.txt", ">", "for_java/output.txt"],
        },
        {
            "type": "java",
            "name": "Solution",
            "request": "launch",
            "mainClass": "for_java.Solution",
            "projectName": "Algo_c7eb0ae5",
            "args":["<", "for_java/input.txt", ">", "for_java/output.txt"],
        }
    ]
}
```