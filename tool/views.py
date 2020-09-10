from django.shortcuts import render
from tool.models import ToolModel, BodyTextModel, ToolPageBackground
from tool.models import EnToolModel, EnBodyTextModel, EnToolPageBackground

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


# english


def en_tool_view(request):
    tool_list = EnToolModel.objects.all()
    background_list = EnToolPageBackground.objects.all()

    context = {
        'tool_list_template': tool_list,
        'background_list_template': background_list}

    return render(request, 'tool/en_tool.html', context)


def en_details(request, entoolmodel_id):
    post_text = EnBodyTextModel.objects.filter(heading_id=entoolmodel_id)
    background_list = EnToolModel.objects.filter(id=entoolmodel_id)

    context = {
        "post_text_details": post_text,
        'background_list_template': background_list
    }

    return render(request, "tool/en_details.html", context)
