"use strict";

const grandCategoryElement = document.querySelector('#id_grand_category');
const parentCategoryElement = document.querySelector('#id_parent_category');
const categoryElement = document.querySelector('#id_category');
const categories = {
            {% for parent in parentcategory_list %}
'{{ parent.pk }}': [
    {% for category in parent.category_set.all %}
{
    'pk': '{{ category.pk }}',
        'name': '{{ category.name }}'
},
{% endfor %}
                ],
{% endfor %}
        };
const categories2 = {
            {% for grand in grandcategory_list %}
'{{ grand.pk }}': [
    {% for category in grand.parentcategory_set.all %}
{
    'pk': '{{ category.pk }}',
        'name': '{{ category.name }}'
},
{% endfor %}
                ],
{% endfor %}
        };
const changeCategory = (select) => {
    const optionAll = document.querySelectorAll('#id_category option');
    for (const option of optionAll) {
        categoryElement.removeChild(option);
    }
    const parentId = parentCategoryElement.value;
    const categoryList = categories[parentId];
    for (const category of categoryList) {
        const option = document.createElement("option")
        option.value = category['pk'];
        option.textContent = category['name'];
        categoryElement.appendChild(option);
    }
    if (select !== undefined) {
        categoryElement.value = select;
    }
};
const changeCategory2 = (select) => {
    const optionAll = document.querySelectorAll('#id_parent_category option');
    for (const option of optionAll) {
        parentCategoryElement.removeChild(option);
    }
    const grandId = grandCategoryElement.value;
    const categoryList2 = categories2[grandId];
    for (const category2 of categoryList2) {
        const option2 = document.createElement("option")
        option2.value = category2['pk'];
        option2.textContent = category2['name'];
        parentCategoryElement.appendChild(option2);
    }
    if (select !== undefined) {
        parentCategoryElement.value = select;
    }
};
parentCategoryElement.addEventListener('change', () => {
    changeCategory();
});
grandCategoryElement.addEventListener('change', () => {
    changeCategory2();
    changeCategory();
});
if (parentCategoryElement.value) {
    changeCategory(categoryElement.value);
}
if (grandCategoryElement.value) {
    changeCategory2(parentCategoryElement.value);
}