from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def main(request): #메인 화면
    return HttpResponse('<h1>메인이얍</h1>')

def login(request): #로그인 화면
    return HttpResponse('<h1>로그인이얍</h1>')

def join(request): #회원가입 화면
    return HttpResponse('<h1>회원가입이얍</h1>')

def swipe(request): #스와이프 화면 ?
    return HttpResponse('<h1>스와이프이얍</h1>')

def like(request): #좋아요 리스트 화면
    return HttpResponse('<h1>좋아요얍</h1>')

def mypage(request): #마이페이지
    return HttpResponse('<h1>마이페이지얍</h1>')

def detail(request): #음식점 상세페이지 O
    return HttpResponse('<h1>상세페이지얍</h1>')
