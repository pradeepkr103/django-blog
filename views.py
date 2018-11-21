# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import blogForm
from django.shortcuts import render,get_object_or_404

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import blog, Comment_block

def index(request):
    category_list = blog.objects.all()
    context = {'category_list': category_list}
    return render(request, 'blog/index.html', context)

def b_detail(request, blog_id):
    content = get_object_or_404(blog, pk=blog_id)
    comments = Comment_block.objects.filter(name__contains=blog_id)
    return render(request, 'blog/post.html', {'blog': content,'comments':comments, 'error_message': "You didn't select a choice.",})


def comment_product(request):
    if request.method == 'POST':
        commentid = request.POST['commentid']
        comment = request.POST['comment']
        commentname = request.POST['commentname']
        print(commentid);
        print(comment);
        print(commentname);

        c = get_object_or_404(blog, pk=commentid)
        c.comment += 1
        c.save()

        Comment_block.objects.create(
            info_id = commentid,
            name = commentid,
            user=commentname,
            comment = comment,
        )

        returncomments = {
            comment, commentid, commentname
        }
        return HttpResponse(returncomments)

# @login_required
def create_blog(request):
    # Handle file upload
    if request.method == 'POST':
        form = blogForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = blog(title = request.POST['title'],content = request.POST['content'], create_date = request.POST['create_date'], image = request.FILES['image'] )

            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect('/blog/blogform/')
    else:
        form = blogForm() # A empty, unbound form

    return render(request, 'blog/blogform.html', {'form': form},

    )
