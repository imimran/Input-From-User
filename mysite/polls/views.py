from django.shortcuts import render

# Create your views here.

def user_info(request):
	print("request data: ", request.POST)

	if request.method =='POST':
		user_name = request.POST ["user_name"]
		context = {"name": user_name}
		return render(request,'froms.html',context)
	return render(request, 'froms.html')




def user_input(request):
	print("request data: ", request.POST)

    if request.method =='POST':
    	user_name=request.POST['user_name']
    	context={"name": user_name}
    	return render(request, 'froms.html', context)




	return render(request, 'froms.html')