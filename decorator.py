def decorate_result(result_function):
    def distinct(marks):
        for i in marks:
            if i>=75:
                print("Distinction")
        result_function(marks)
     return distinct  

@decorate_result

def result(marks):
    for i in marks:
        if i>=33:
            pass
        else:
            print('FAIL')
            break
    else:
        print("PASS");

result([34,43,55,53,42])