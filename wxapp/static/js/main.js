function getUploaderImgName(uploaderContainerId) {
    let imgName = $(uploaderContainerId).css('backgroud-image');
    if (imgName != 'none') {
        imgName = imgName.substring(imgName.lastIndexOf('/') + 1, imgName.length - 2);
    }
    return imgName;
} 

function getUploaderImgNameInJSON(uploaderContainerId) {
    return jQuery.parseJSON('{ "img": "' + getUploaderImgName(uploaderContainerId) + '" }')
}

function getUploaderImgNameInObject(uploaderContainerId) {
    return {
        img:getUploaderImgName(uploaderContainerId)
    }
}

function generateUploader(uploaderContainerId, uploaderId, removeId) {
        $(uploaderId).uploadify({
        'swf'      : 'http://127.0.0.1:5000/static/js/uploadify.swf',
        'uploader' : 'http://127.0.0.1:5000/upload',
        'height' : 200,
        'width' : 200,
        'buttonText' : '+ 上传',
        'buttonClass' : 'uploadbuttonstyle',
        'method'   : 'post',
        'multi' : false,
        'formData' : getUploaderImgNameInJSON(uploaderContainerId),
        'itemTemplate' : '<p></p>',
        'onUploadSuccess' : function(file, data, response) {
            $(uploaderId).css("opacity",'0');
            $(uploaderContainerId).css("background-image",'url("' + data + '")');
            $(uploaderId).uploadify('settings', 'formData', getUploaderImgNameInJSON(uploaderContainerId));
            var files = $('#imageupload').data('uploadify').queueData.files = [];
            for (var member in files) 
                delete files[member];
            if ($(uploaderContainerId).find(removeId).length == 0) {
                $(uploaderContainerId).append('<div id="remove">删除图片</div>')
            }

            $(removeId).css('display','none'); 

            $(uploaderContainerId).mouseover(function(){
                $(removeId).css('display','block'); 
            });
            $(uploaderContainerId).mouseout(function(){
                $(removeId).css('display','none');                            
            });

            $(removeId).click(function(){
                $.ajax({
                        // The URL for the request
                        url: "http://127.0.0.1:5000/delete",
                    
                        // The data to send (will be converted to a query string)
                        data: getUploaderImgNameInObject(uploaderContainerId),
                    
                        // Whether this is a POST or GET request
                        type: "POST",
                        // The type of data we expect back
                        dataType : "json",
                    })
                    // Code to run if the request succeeds (is done);
                    // The response is passed to the function
                    .done(function( json ) {
                        alert('delete suceessfully' + json)
                    })
                    // Code to run if the request fails; the raw request and
                    // status codes are passed to the function
                    .fail(function( xhr, status, errorThrown ) {
                        alert( "Sorry, there was a problem!" );
                    })
                    // Code to run regardless of success or failure;
                    .always(function( xhr, status ) {
                        alert( "The request is complete!" );
                    });
            });
        },
    });
}