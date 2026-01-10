from django.shortcuts import render


def board_list(request):
    """게시판 목록 뷰"""
    return render(request, 'board/board_list.html')

