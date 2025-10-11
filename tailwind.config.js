module.exports = {
    content: [
        "./templates/**/*.html", // Django template 경로 지정
        "./**/*.py", // 필요시, Python 파일 내부의 템플릿 문자열까지
    ],
    theme: {
        extend: {},
    },
    plugins: [],
}