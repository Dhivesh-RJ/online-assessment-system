from django.shortcuts import render, get_object_or_404, redirect
from .models import Test, Question, Result
from .models import Result

def test_list(request):
    tests = Test.objects.all()
    return render(request, 'test_list.html', {'tests': tests})

def take_test(request, test_id):
    test = get_object_or_404(Test, pk=test_id)
    questions = test.questions.all()
    return render(request, 'take_test.html', {
        'test': test,
        'questions': questions
    })

def submit_test(request):
    if request.method == 'POST':
        test_id = request.POST.get('test_id')
        student_name = request.POST.get('student_name')
        test = get_object_or_404(Test, pk=test_id)
        questions = test.questions.all()
        score = 0

        for question in questions:
            selected_option = request.POST.get(f'q{question.id}')
            if selected_option == question.correct_option:
                score += 1

        Result.objects.create(student_name=student_name, test=test, score=score)

        return render(request, 'result.html', {
            'student_name': student_name,
            'test': test,
            'score': score,
            'total': questions.count()
        })
    else:
        return redirect('test_list')
def all_results(request):
    results = Result.objects.all().order_by('-id')  # Latest first
    return render(request, 'all_results.html', {'results': results})