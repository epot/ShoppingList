from django.shortcuts import render, get_object_or_404
from shopping.models import Recipe, RecipeElement
from django.http import HttpResponseRedirect, HttpResponse

from django.contrib.auth.decorators import login_required

@login_required(login_url='/shopping/accounts/login/')
def index(request):
    latest_recipe_list = Recipe.objects.order_by('-creation_date')[:5]
    print latest_recipe_list
    context = {'latest_recipe_list': latest_recipe_list}
    return render(request, 'shopping/index.html', context)

def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'shopping/recipe_detail.html', {'recipe': recipe, 'elements': RecipeElement.objects.filter(recipe=recipe)})


def addelement(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return HttpResponse("coin")
    """try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))"""