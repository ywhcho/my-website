from django.shortcuts import render


def medicine_info(request):
    """의약정보 조회 뷰"""
    return render(request, 'medicine/medicine_info.html')

