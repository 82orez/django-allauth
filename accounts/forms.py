from django import forms
from allauth.account.forms import SignupForm
from .models import User


class CustomSignupForm(SignupForm):
    name = forms.CharField(
        max_length=150,
        label="이름",
        help_text="실명을 입력해 주세요.",
        widget=forms.TextInput(attrs={"placeholder": "홍길동"}),
    )

    terms_agreement = forms.BooleanField(
        label="이용약관 및 개인정보처리방침 동의",
        help_text="서비스 이용을 위해 필수 약관에 동의해 주세요.",
        required=True,
        error_messages={"required": "이용약관 및 개인정보처리방침에 동의해야 합니다."},
    )

    privacy_agreement = forms.BooleanField(
        label="개인정보 수집 및 이용 동의",
        help_text="개인정보 수집 및 이용에 동의해 주세요.",
        required=True,
        error_messages={"required": "개인정보 수집 및 이용에 동의해야 합니다."},
    )

    def save(self, request):
        # 기본 allauth의 save 메서드 호출하여 사용자 생성
        user = super().save(request)

        # 추가 필드 값을 사용자에게 설정
        user.name = self.cleaned_data.get("name", "")
        user.save()

        return user

    class Meta:
        model = User
        fields = (
            "email",
            "name",
            "password1",
            "password2",
            "terms_agreement",
            "privacy_agreement",
        )
