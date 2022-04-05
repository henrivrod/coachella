$(document).ready(function () {
    let i = 0
    let j = 0
    let k = 0
    $("#addconcession").click(function () {
        if (i < 1) {
            i += 1;
            $("#area_id").append("<div><input type='text' name='area_identry' placeholder = 'area id'></div>");
            //$("#tent_id").append("<label for='tent_identry' id='tentid_warning'></label>");
            $("#con_stage_id").append("<div><input type='text' name='con_stage_identry' placeholder = 'stage id'></div>");
            //$("#stage_id").append("<label for='stage_identry' id='stageid_warning'></label>");
            $("#area_name").append("<div><input type='text' name='area_nameentry' placeholder = 'Area Name'></div>");
            //$("#num_workers").append("<label for='num_workersentry' id='numworkerswarning'></label>");
            $("#number_of_stands").append("<div><input type='text' name='num_standsentry' placeholder = 'Number of Stands'></div>");
            $("#concessionbutton").append("<input type='submit' value='Submit'>");
            $("#addbuttonconcession").empty();
            $("#standhead").empty();
            $("#dishhead").empty();
            $("#addbuttonstand").empty();
            $("#addbuttondish").empty();
        }
    });

    $("#addstand").click(function () {
        if (j < 1) {
            j += 1;
            $("#stand_id").append("<div><input type='text' name='stand_identry' placeholder = 'stand id'></div>");
            //$("#tent_id").append("<label for='tent_identry' id='tentid_warning'></label>");
            $("#stand_area_id").append("<div><input type='text' name='stand_areaidentry' placeholder = 'Area id'></div>");
            //$("#stage_id").append("<label for='stage_identry' id='stageid_warning'></label>");
            $("#stand_name").append("<div><input type='text' name='stand_nameentry' placeholder = 'Stand Name'></div>");
            //$("#num_workers").append("<label for='num_workersentry' id='numworkerswarning'></label>");
            $("#standbutton").append("<input type='submit' value='Submit'>");
            $("#addbuttonstand").empty();
            $("#conhead").empty();
            $("#dishhead").empty();
            $("#addbuttonconcession").empty();
            $("#addbuttondish").empty();
        }
    });

    $("#adddish").click(function () {
        if (k < 1) {
            k += 1;
            $("#dish_id").append("<div><input type='text' name='dish_identry' placeholder = 'dish id'></div>");
            //$("#tent_id").append("<label for='tent_identry' id='tentid_warning'></label>");
            $("#dish_stand_id").append("<div><input type='text' name='dish_stand_identry' placeholder = 'stand id'></div>");
            //$("#stage_id").append("<label for='stage_identry' id='stageid_warning'></label>");
            $("#dish_name").append("<div><input type='text' name='dish_nameentry' placeholder = 'Dish Name'></div>");
            //$("#num_workers").append("<label for='num_workersentry' id='numworkerswarning'></label>");
            $("#dish_price").append("<div><input type='text' name='dish_priceentry' placeholder = 'Dish Price'></div>");
            //$("#num_workers").append("<label for='num_workersentry' id='numworkerswarning'></label>");
            $("#dish_item_type").append("<div><input type='text' name='dish_item_typeentry' placeholder = 'Item Type'></div>");
            //$("#num_workers").append("<label for='num_workersentry' id='numworkerswarning'></label>");
            $("#dishbutton").append("<input type='submit' value='Submit'>");
            $("#addbuttondish").empty();
            $("#standhead").empty();
            $("#conhead").empty();
            $("#addbuttonstand").empty();
            $("#addbuttonconcession").empty();
        }
    });

});