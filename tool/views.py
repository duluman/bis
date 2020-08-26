from django.shortcuts import render
from tool.models import ToolModel, BodyTextModel, ToolPageBackground

# Create your views here.


def tool_view(request):
    tool_list = ToolModel.objects.all()
    background_list = ToolPageBackground.objects.all()

    context = {
        'tool_list_template': tool_list,
        'background_list_template': background_list}

    return render(request, 'tool/tool.html', context)


def details(request, toolmodel_id):
    post_text = BodyTextModel.objects.filter(heading_id=toolmodel_id)
    background_list = ToolModel.objects.filter(id=toolmodel_id)

    context = {
        "post_text_details": post_text,
        'background_list_template': background_list
    }

    return render(request, "tool/details.html", context)

