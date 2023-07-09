from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

import markdown2
from . import util

from difflib import get_close_matches
import random

def entryExist(entry):
  if entry in util.list_entries():
    return True
  else:
    return False
  
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entryPage(request, entry):
    entrys = util.list_entries()
    if entryExist(entry):
      return render(request, "encyclopedia/entry.html", {
				  "entry": entry, 
          "content": markdown2.markdown(util.get_entry(entry))
			})
    else:
      return render(request, "encyclopedia/error.html", {
         "entry":markdown2.Markdown().convert(f"{entry}:_No such entry in encyclopedia_")
			})     

def add(request):
  if request.method == 'POST':
    data = request.POST.dict()
    title = data.get("title")
    content = data.get("body")
    if entryExist(title):
      return render(request, "encyclopedia/error.html", {
         "entry":markdown2.Markdown().convert(f"{title}:*That entry already exist*")
			}) 
    else:
      util.save_entry(title, content)
      return render(request, "encyclopedia/entry.html", {
		"entry": title, 
        	"content": markdown2.markdown(util.get_entry(title))
			})
	  # return HttpResponseRedirect(reverse("index") )
  else:
	  return render(request, 'encyclopedia/add.html')


def edit(request):
   if request.method == 'POST':
      data = request.POST["entry"]
      return render(request, "encyclopedia/edit.html", {
        "entry": data, 
        "content": util.get_entry(data)
			})

def update(request):
  if request.method == 'POST':
    data = request.POST.dict()
    title = data.get("title")
    content = data.get("body")
    util.save_entry(title, content)
    return render(request, "encyclopedia/entry.html", {
				  "entry": title, 
          "content": markdown2.markdown(util.get_entry(title))
			})
    # return HttpResponseRedirect(reverse("index") )
  
def search(request):
  if request.method == "POST":
    entry = request.POST["q"]
    if entryExist(entry):
       return render(request, "encyclopedia/entry.html", {
		"entry": entry, 
		"content": markdown2.markdown(util.get_entry(entry))
		})
    else:
        result = get_close_matches(entry, util.list_entries())
        return render(request, "encyclopedia/search.html", {
					"query": entry,
			"entries": result
		})
  

def randomEntry(request):
  list = util.list_entries()
  number = random.randint(1, len(list)) - 1
  entry = list[number]
  return render(request, "encyclopedia/entry.html", {
	"entry": entry, 
    "content": markdown2.markdown(util.get_entry(entry))
	})
