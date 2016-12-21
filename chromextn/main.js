var gmail;

function action_refresh(f) {
  if( (/in/.test(document.readyState)) || (typeof Gmail === undefined) ) {
    setTimeout('action_refresh(' + f + ')', 10);
  } else {
    f();
  }
}

function action_auto_expand(obj) {
    if (!obj.savesize) obj.savesize=obj.size;
      obj.size=Math.max(obj.savesize,obj.value.length);
}

var main = function(){
  gmail = new Gmail();
  console.log('Hello,', gmail.get.user_email())


  function open_assistant_window(title, content_html, onClickOk, onClickOkText, onClickCancel,
    onClickCancelText, onClickClose) {
    // By default, clicking on cancel or close should clean up the modal window
    onClickOk = onClickOk || close_assistant_window;
    onClickClose = onClickClose || close_assistant_window;
    onClickCancel = onClickCancel || close_assistant_window;
    onClickOkText = onClickOkText || "OK"
    onClickCancelText = onClickCancelText || "Cancel"

    var background = $(document.createElement('div'));
    background.attr('id','gmailJsModalBackground');
    background.attr('class','Kj-JD-Jh');
    background.attr('aria-hidden','true');
    background.attr('style','opacity:0.75;width:100%;height:100%;');

    // Modal window wrapper
    var container = $(document.createElement('div'));
    container.attr('id','gmailJsModalWindow');
    container.attr('class', 'Kj-JD');
    container.attr('tabindex', '0');
    container.attr('role', 'alertdialog');
    container.attr('aria-labelledby', 'gmailJsModalWindowTitle');
    container.attr('style', 'left:50%;top:50%;opacity:1;');

    // Modal window header contents
    var header = $(document.createElement('div'));
    header.attr('class', 'Kj-JD-K7 Kj-JD-K7-GIHV4');
    header.attr('style', 'height:40px;');

    var heading = $(document.createElement('span'));
    heading.attr('id', 'gmailJsModalWindowTitle');
    heading.attr('class', 'Kj-JD-K7-K0');
    heading.attr('role', 'heading');
    heading.attr('style', 'margin:0px; width: calc(100% - 60px); text-overflow: ellipsis;');
    heading.html(title);

    var closeButton = $(document.createElement('span'));
    closeButton.attr('id', 'gmailJsModalWindowClose');
    closeButton.attr('class', 'Kj-JD-K7-Jq');
    closeButton.attr('role', 'button');
    closeButton.attr('tabindex', '0');
    closeButton.attr('style', 'cursor: pointer');
    closeButton.attr('aria-label', 'Close');
    closeButton.click(onClickClose);

    header.append(heading);
    header.append(closeButton);

    // Modal window contents
    var contents = $(document.createElement('div'));
    contents.attr('id', 'gmailJsModalWindowContent');
    contents.attr('class', 'Kj-JD-Jz');
    contents.attr('style', 'width:100%; height: calc(100% - 90px);')
    if (typeof content_html === 'string')
        contents.html(content_html);
    else
        contents.append(content_html);

    // Modal window controls
    var controls = $(document.createElement('div'));
    controls.attr('class', 'Kj-JD-Jl');
    controls.attr('style', 'height:30px; margin:0px');

    var okButton = $(document.createElement('button'));
    okButton.attr('id', 'gmailJsModalWindowOk');
    okButton.attr('class', 'J-at1-auR J-at1-atl');
    okButton.attr('name', 'ok');
    okButton.text(onClickOkText);
    okButton.click(onClickOk);

    var cancelButton = $(document.createElement('button'));
    cancelButton.attr('id', 'gmailJsModalWindowCancel');
    cancelButton.attr('name', 'cancel');
    cancelButton.text(onClickCancelText);
    cancelButton.click(onClickCancel);

    controls.append(okButton);
    controls.append(cancelButton);

    container.append(header);
    container.append(contents);
    container.append(controls);

    $(document.body).append(background);
    $(document.body).append(container);

    var center = function() {
      container.css({
        top: (50),
        height: ($(window).height() - (container.outerHeight() - container.height()) - 100),
        left: (100),
        width: ($(window).width() - (container.outerWidth() - container.width()) - 200)
      });
    };

    center();

    $(window).resize(center);
  };

  function close_assistant_window() {
    $('#gmailJsModalBackground').remove();
    $('#gmailJsModalWindow').remove();
  }

  var construct_html = {
    construct_input_FT : function(data) {
        var content = $(document.createElement('div'));
        var html = "";
        html += '<div style="padding-left: 2px;padding-top:5px; padding-bottom:5px; width:100%"><div style="padding-bottom:8px">'
        html += data.label + '</div>'
        html += '<div contenteditable style="border-bottom: 1px solid #cfcfcf;outline: none; width:100%;'
        html += 'word-wrap:break-word; overflow-wrap:break-word; white-space:normal"></div></div>'
        content.html(html);
        return content;
    },
    construct_input_A : function(data) {
        return null
    },
    construct_input_DT : function(data) {
    },
    construct_input_NUM : function(data) {
    },
    construct_input_LOC : function(data) {
    },
    construct_input_YN : function(data, i) {
        var content = $(document.createElement('div'));
        var html = "";
        html += '<div style="padding-left: 2px;padding-top:5px; padding-bottom:5px"><div style="padding-bottom:8px">'
        html += data.label + '</div>'
        html += '<input type="radio" name = "radio_' + i +  '" /> Yes &nbsp;&nbsp;'
        html += '<input type="radio" name = "radio_' + i +  '" /> No &nbsp;&nbsp;'
        html += '<div contenteditable style="border-bottom: 1px solid #cfcfcf;outline: none; padding-top:8px"></div></div>'
        content.html(html);
        return content;
    },
    construct_input_TAREA : function(data) {
    },
    construct_input_LST : function(data) {
    },
    construct : function(data, content_email) {
        var content = $(document.createElement('div'));
        content.attr('style', 'width: 100%; height: 100%')
        var html = "";
        html += '<div style="width: 100%; height:100%; display: flex;">'
        html += '<div class="assistant_content_ui" style="width: 50%; height:100%; overflow-y:auto; padding:10px"></div>'
        html += '<div class="assistant_content_email" style="width: 50%; height:100%; overflow-y:auto; padding:10px;'
        html += 'border-left: 1px solid #cfcfcf"></div>'
        html += '</div></div>'
//        html += '<table style="width:100%;height:100%;border:0"><tbody style="width:100%;height:100%;">'
//            + '<tr style="width:100%;height:100%">'
//            + '<td class="assistant_content_ui" style = "width:50%; height:100%; overflow-y: auto"></td>'
//            + '<td class="assistant_content_summary" style = "width:50%; height:100%; overflow-y: auto"></td></tr></tbody></table>';
        content.html(html);
        var ui_content = content.find('.assistant_content_ui');
        for(i in data) {
            var ui_element_content = construct_html["construct_input_" + data[i].type](data[i], i);
             if (ui_element_content)
                ui_content.append(ui_element_content);
        }
        var email_content = content.find('.assistant_content_email');
        email_content.append($(content_email).clone())
        return content;
    }
  };

  gmail.observe.on('view_thread', function(obj) {
    var thread = gmail.dom.thread(obj.$el)
    var imgUrl = $("#--action-img-url").val()
    var ele = '<td class="gH"><div class="T-I J-J5-Ji T-I-Js-IF aaq T-I-ax7 L3" role="button"'
    + 'data-tooltip="Assistant" style="user-select: none; padding:0px; margin-top: -6px; margin-right:4px;">'
    + '<img style="font-size: 21px; width: 21px; height: 21px; opacity: .55; margin-top: 3px;"'
    + 'role="button" src="' + imgUrl + '" alt=""></div></td>';

    ele = $.parseHTML(ele);
    $(ele).click({

    }, open_modal);

    function open_modal(event) {
        $.ajax({
          dataType: "json",
          url: "http://localhost:5000/parse_and_classify",
          method: "POST",
          data: {data : $(thread.email_contents()).text()},
          success: function(data) {
            open_assistant_window($(thread.email_subject()).text(), construct_html.construct(data, thread.email_contents()));
          }
        });
    }

    $(ele).insertBefore($(thread.email_body()).find(".acX"));

  });


}


action_refresh(main);