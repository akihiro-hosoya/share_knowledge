//地域セレクトボックスイベント設定
setHierarchySelectEvent('#select1', '#select2');
// setHierarchySelectEvent('#area2', '#area3');
//セレクトボックスの初期値
$('#select1').val('').change();
$('#select2').val('').change();
// 


/**
 * 階層のあるプルダウンのイベントを設定します.
 * 親のselectタグには属性data-subgroupが設定されている必要があります。
 * 子のselectタグには属性data-groupが設定されている必要があります。
 * @param parentSelect 親となるselectタグのセレクタ
 * @param childSelect 子となるselectタグのセレクタ
 */

function setHierarchySelectEvent(parentSelect, childSelect){
    var initCategorySmallHtml = $(childSelect).html();
    $(parentSelect).change(function(){
        if( 1 < $(this).find('option:selected').length ){
            $(childSelect).find("option").each(function(index, element){
                $(element).remove();
            });
        }else{
            var subgroup =  $(this).find('option:selected').attr('data-subgroup');
            $(childSelect).html(initCategorySmallHtml);
            $(childSelect).find("option").each(function(index, element){
                var group = $(element).attr('data-group');
                if( group ){
                    if( subgroup == group ){
                        //$(element).css('display', 'block');//IEではoptionタグに対してdisplayは効かないため
                    }else{
                        //$(element).css('display', 'none');//IEではoptionタグに対してdisplayは効かないため
                        $(element).remove();
                    }
                }
            });
        }
        $(childSelect).val('').change();//未選択時の値は''じゃない場合は書き換えてね
    });
}