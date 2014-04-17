/*  
 *  Copyright (c) 2012, 2013 Jochen S. Klar <jklar@aip.de>,
 *                           Adrian M. Partl <apartl@aip.de>, 
 *                           AIP E-Science (www.aip.de)
 *
 *  Licensed under the Apache License, Version 2.0 (the "License");
 *  you may not use this file except in compliance with the License.
 *  See the NOTICE file distributed with this work for additional
 *  information regarding copyright ownership. You may obtain a copy
 *  of the License at
 *
 *  http://www.apache.org/licenses/LICENSE-2.0
 *
 *  Unless required by applicable law or agreed to in writing, software
 *  distributed under the License is distributed on an "AS IS" BASIS,
 *  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *  See the License for the specific language governing permissions and
 *  limitations under the License.
 */

// namespaces
var jk = jk || {}; jk.table = {};

/**
 * jquery plugin to insert a table in a given jquery selection
 */
(function($){
    $.fn.extend({ 
        jk_table: function(opt) {
            opt = $.extend({}, jk.table.opt, opt);
            return this.each(function() {
                var id = $(this).attr('id');
                // check if table is already set
                if (jk.table.items[id] == undefined) {
                    jk.table.items[id] = new jk.table.Table($(this),opt);
                } else {
                    jk.table.items[id].reinit(opt);
                }
            });
        }
    });
})(jQuery);

/**
 * Object to hold the different instances of the Table class.
 */
jk.table.items = {};

/**
 * Object to hold the information to resize a column.
 */
jk.table.resizing = null;

/**
 * Object to hold the default option of the table.
 */
jk.table.opt = {
    'header' : {},
    'nrows': 10,
    'nrowsList': [10,100],
    'sort': null,
    'columnWidth': '100px',
    'multiselect': false,
    'trans': {
        'Search': 'Search',
        'First': 'First',
        'Previous': 'Previous',
        'Next': 'Next',
        'Last': 'Last',
        'Reset': 'Reset',
        'Page': 'Page',
        'of': 'of',
        'Show': 'Show',
        'Rows': 'Rows'
    }
};

/**
 * Constructor-like function for the Table class. 
 */
jk.table.Table = function(container, opt) {
    this.container = container;
    this.id = container.attr('id');
    this.opt = $.extend({}, jk.table.opt, opt);
    params = null;
    pages = null;
    ncols = null;
    colsmodel = null;
    console.log(this.id);
    // assign this table to the globel array of tables
    jk.table.items[this.id] = this;

    // create pager
    $('<div/>',{
        'class': 'jk-table-pager'
    }).appendTo(this.container);
    
    // create pane for table
    $('<div/>',{
        'class': 'jk-table-pane',
        'html': '<table class="table"><thead></thead><tbody></tbody></table>'
    }).appendTo(this.container);

    // create message
    $('<div/>',{
        'class': 'jk-table-message'
    }).appendTo(this.container);

    // set class
    this.container.addClass('jk-table');

    // initial params
    this.params = {
        'nrows': this.opt.nrows,
        'page': 1,
        'sort': this.opt.sort,
        'search': null
    };

    // display table
    this.pager();
    this.cols();
};

/**
 * Resets the table to its inital state and overwrites the opt object.
 */
jk.table.Table.prototype.reinit = function (opt) {
    this.opt = opt;

    $('thead','.jk-table-pane', this.container).children().remove();
    $('tbody','.jk-table-pane', this.container).children().remove();
    $('.jk-table-pager', this.container).children().remove();
    $('.jk-table-message', this.container).children().remove();
    
    // initial params
    this.params = {
        'nrows': this.opt.nrows,
        'page': 1,
        'sort': this.opt.sort,
        'search': null
    };
    
    // display table
    this.pager();
    this.cols();
}

/**
 * Switches the table to the fist page.
 */
jk.table.Table.prototype.first = function (callback) {
    if (this.params.page != 1) {
        this.params.page = 1;
        this.rows(callback);
    } else {
        callback();
    }
}

/**
 * Switches the table to the previous page.
 */
jk.table.Table.prototype.prev = function (callback) {
    this.params.page -= 1; 
    if (this.params.page < 1) {
        this.params.page = 1;
        callback();
    } else {
        this.rows(callback);
    }
}

/**
 * Switches the table to the next page.
 */
jk.table.Table.prototype.next = function (callback) {
    this.params.page += 1;
    if (this.params.page > this.pages) {
        this.params.page = this.pages;
        callback();
    } else {
        this.rows(callback);
    }
}

/**
 * Switches the table to the last page.
 */
jk.table.Table.prototype.last = function (callback) {
    if (this.params.page != this.pages) {
        this.params.page = this.pages;
        this.rows(callback);
    } else {
        callback();
    }
}

/**
 * Switches the table to the last page.
 */
jk.table.Table.prototype.reset = function () {
    $('input','.jk-table-pager-search-form', this.container).val('');
        
    this.params.search = null
    this.params.sort = null
    this.params.page = 1
    this.rows();
}

/**
 * Constructs and displays the pager at the bottom of the table.
 */
jk.table.Table.prototype.pager = function () {
    var self = this;

    var searchHtml = '<div class="input-group" style="width: 250px;">';
    searchHtml += '<input id="' + self.id + '-pager-search-input" placeholder="' + self.opt.trans.Search + '" type="text" class="form-control" />';
    searchHtml += '<a href="#" class="input-group-addon"><span class="glyphicon glyphicon-search"></span></a>';
    searchHtml += '</div>';

    var search = $('<form/>',{
        'id': self.id + '-pager-search',
        'class': 'jk-table-pager-search-form input-append pull-left',
        'html': searchHtml
    }).submit(function () {
        var id = $(this).attr('id').match(/(.+)-pager-search/)[1];
        var self = jk.table.items[id];
        self.params.search = $('input',this).val()
        self.rows();
        return false;
    }).appendTo($('.jk-table-pager', self.container));

    $('#' + self.id + '-pager-search').click(function () {
        $(this).parent().submit();
        return false;
    });

    html = '<li><a id="' + self.id + '-pager-first" href="#">' + self.opt.trans.First + '</a></li>';
    html += '<li><a id="' + self.id + '-pager-prev" href="#">' + self.opt.trans.Previous + '</a></li>';
    html += '<li><a id="' + self.id + '-pager-next" href="#">' + self.opt.trans.Next + '</a></li>';
    html += '<li><a id="' + self.id + '-pager-last" href="#">' + self.opt.trans.Last + '</a></li>';

    $('<ul />', {
        'id': self.id + '-pager-pagination',
        'class': 'pagination pull-left',
        'html': html
    }).appendTo($('.jk-table-pager', self.container));
    
    $('<ul />', {
        'id': self.id + '-pager-reset',
        'class': 'pagination pull-left',
        'html': '<li><a href="#">' + self.opt.trans.Reset + '</a></li>'
    }).appendTo($('.jk-table-pager', self.container));

    $('#' + self.id + '-pager-first').click(function () {
        var id = $(this).attr('id').match(/(.+)-pager-first/)[1];
        var self = jk.table.items[id];
        self.params.page = 1;
        self.rows();
        return false;
    });
    
    $('#' + self.id + '-pager-prev').click(function () {
        var id = $(this).attr('id').match(/(.+)-pager-prev/)[1];
        var self = jk.table.items[id];
        self.params.page -= 1; 
        if (self.params.page < 1) {
            self.params.page = 1;
        }
        self.rows();
        return false;
    });

    $('#' + self.id + '-pager-next').click(function () {
        var id = $(this).attr('id').match(/(.+)-pager-next/)[1];
        var self = jk.table.items[id];
        self.params.page += 1;
        if (self.params.page > self.pages) {
            self.params.page = self.pages;
        }
        self.rows();
        return false;
    });
    
    $('#' + self.id + '-pager-last').click(function () {
        var id = $(this).attr('id').match(/(.+)-pager-last/)[1];
        var self = jk.table.items[id];
        self.params.page = self.pages;
        self.rows();
        return false;
    });

    $('#' + self.id + '-pager-reset').click(function () {
        var id = $(this).attr('id').match(/(.+)-pager-reset/)[1];
        var self = jk.table.items[id];
        
        $('input','.jk-table-pager-search-form', self.container).val('');
            
        self.params.search = null
        self.params.sort = null
        self.params.page = 1
        self.rows();
        return false;
    });

    $('<div/>',{
        'class': 'jk-table-pager-paging pull-left',
        'id': self.id + '-pager-paging'
    }).appendTo($('.jk-table-pager', self.container));

    var select = $('<select/>',{
        'size': self.opt.nrowsList.length,
        'class': 'jk-table-pager-nrows pull-right form-control',
        'id': self.id + '-pager-nrows'
    }).appendTo($('.jk-table-pager', self.container));

    $.each(self.opt.nrowsList, function (key, value) {
        var option = {
            'value': value,
            'html': self.opt.trans.Show + ' ' + value + ' ' + self.opt.trans.Rows
        };
        if (self.opt.nrows == value) {
            option.selected = 'selected';
        }
        $('<option/>', option).appendTo(select);
    });

    $('#' + self.id + '-pager-nrows').change( function() {
        var id = $(this).attr('id').match(/(.+)-pager-nrows/)[1];
        var self = jk.table.items[id];
        self.params.page = 1;
        self.params.nrows = $(this).val();
        self.rows();
    });
}

/**
 * Gets the colums by ajax and constructs the th elements. On success it calls the rows function.
 */
jk.table.Table.prototype.cols = function () {
    var self = this;

    // get the cols via ajax
    $.ajax({
        url: self.opt.colsurl, 
        type: 'GET',
        data: $.extend({}, self.opt.params, self.params),
        dataType: 'json',
        headers: $.extend({}, self.opt.header, {
            'Accept': 'application/json'
        }),
        success: function (json) {
            self.ncols = json.cols.length;
            self.colsmodel  = json.cols;

            // contruct and append html elements for column headers
            var html = '<tr>';
            var width,colId;
            for (var i = 0; i < self.ncols; i++) {
                // get the id of the column
                colId = self.colsmodel[i]['id'];
                // if (typeof colId === 'undefined') colId = i;

                if (self.colsmodel[i].hidden != true) {
                    if (self.colsmodel[i].width != undefined) {
                        width = self.colsmodel[i].width;
                    } else {
                        width = self.opt.colsWidth;
                    }
                    classes = 'jk-table-col-' + colId;
                    if (self.colsmodel[i].sortable != 'false') {
                        classes += ' sortable';
                    }
                    html += '<th id="' + self.id + '-thead-col-' + colId + '" style="width:' + width + '" class="' + classes + '">';
                    if (i != 0) {
                        html += '<div class="handle-left pull-left"></div>';
                    }
                    html += '<span>' + self.colsmodel[i].verboseName + '</span>';
                    html += '<div class="handle-right pull-right"></div>';
                    if (self.colsmodel[i].sortable == 1) {
                        html += '<span id="' + self.id + '-thead-sort" class="glyphicon glyphicon-chevron-down pull-right"></span>';
                    }
                    html += '</th>';
                }
            }
            html += '</tr>';
            $('thead',self.container).append(html);

            $('th', self.container).click(function () {
                var id = $(this).attr('id').match(/(.+)-thead-col-\d+/)[1];
                var self = jk.table.items[id];
                
                // determine which column was clicked
                var element = $(this)
                var classes = element.attr('class');
                var colClass = classes.match(/jk-table-col-\d+/)[0];
                
                // remove 'selected' class from other elements and add to this column
                $('.jk-table-col-selected', 'table', self.container).removeClass('jk-table-col-selected');

                if (classes.indexOf('jk-table-col-selected') == -1) {
                    // add 'selected' class to column header
                    $('.' + colClass, self.container).addClass('jk-table-col-selected');
                }
            });
            
            // add sorting function to click on header
            $('span', 'th', self.container).click( function () {
                var id = $(this).attr('id').match(/(.+)-thead-sort/)[1];
                var self = jk.table.items[id];

                // determine which column was clicked
                var element = $(this);
                var classes = element.attr('class');
                var colId = element.parent().attr('id').match(/thead-col-(\d+)/)[1];
                var colName = self.colsmodel[colId].name;
                        
                // manipulate arrow and change sort options
                if (classes.indexOf('sorted') == -1) {
                    $('.sorted', self.container).removeClass('sorted').removeClass('glyphicon-chevron-up').addClass('glyphicon-chevron-down');
                    element.addClass('sorted');
                    element.addClass('glyphicon-chevron-down');
                    self.params.sort = colName + ' ASC';
                } else {
                    if (element.attr('class').indexOf('glyphicon-chevron-down') != -1) {
                        element.removeClass('glyphicon-chevron-down').addClass('glyphicon-chevron-up');
                        self.params.sort = colName + ' DESC';
                    } else {
                        element.removeClass('glyphicon-chevron-up').addClass('glyphicon-chevron-down');
                        self.params.sort = colName + ' ASC';
                    }
                }
                        
                // display new set of rows
                self.rows();

                // return but do not trigger click event in parent th
                return false;
            });
            
            // make columns resizsable
            // disable click events on handle divs left an right of the header
            $('.handle-right').click(function () {
                return false;
            });
            $('.handle-left').click(function () {
                return false;
            });
            
            // on mousedown, init global resizing object
            $('.handle-right').on('mousedown', function (e) {
                var match = $(this).parent().attr('id').match(/(.+)-thead-col-(\d+)/);
                var id = match[1];
                var colId = match[2];
                var self = jk.table.items[id];
                var cols = $('th.jk-table-col-' + colId, self.container);
                
                jk.table.resizing = {
                    'cols': cols,
                    'zero': e.pageX,
                    'width': $('th.jk-table-col-' + colId, self.container).width()
                }
            });
            $('.handle-left').on('mousedown', function (e) {
                var match = $(this).parent().attr('id').match(/(.+)-thead-col-(\d+)/);
                var id = match[1];
                var colId = match[2];
                var self = jk.table.items[id];
                var cols = $('th.jk-table-col-' + (colId - 1), self.container);

                jk.table.resizing = {
                    'cols': cols,
                    'zero': e.pageX,
                    'width': $('th.jk-table-col-' + (colId - 1), self.container).width()
                }
                return false;
            });
            
            // on mouse up remove resizing object
            $(document).on('mouseup', function () {
                if (jk.table.resizing != null) {
                    jk.table.resizing = null;
                }
            });
            
            // on mousemove perform resizing if resizing object is not null
            $(document).on("mousemove", function(e) {
                if (jk.table.resizing != null) {
                    var delta = e.pageX - jk.table.resizing.zero;

                    var width = jk.table.resizing.width + delta;
                    if (width < 50) {
                        width = 50;
                    }
                    jk.table.resizing.cols.width(width);
                }
            });
            
            // display new set of rows
            self.rows();
        }
    });
}

/**
 * Gets the rows by ajax and constructs the td elements. On success it calls an optional function.
 */
jk.table.Table.prototype.rows = function (callback) {
    var self = this;

    // get the rows via ajax
    $.ajax({
        url: self.opt.rowsurl, 
        type: 'GET',
        data: $.extend({}, self.opt.params, self.params),
        dataType: 'json',
        headers: $.extend({}, self.opt.header, {
            'Accept': 'application/json'
        }),
        success: function (json) {
            // store information from server in params
            self.pages = json.pages;

            // update pager
            var html = '<p>' + self.opt.trans.Page + ' ' + json.page + ' ' + self.opt.trans.of + ' ' + json.pages;
            var paging = $('#' + self.id + '-pager-paging');
            paging.children().remove();
            paging.append(html);

            // get the id of the selected column
            var selected = $('.jk-table-col-selected');
            if (selected.length != 0) {
                var selectedId = selected.attr('class').match(/jk-table-col-(\d+)/)[1];
            }

            // construct html elements for the rows
            html = '';
            var i,j,classes,text,format,rowId,colId,cell,ext;
            for (j = 0; j < json.nrows; j++) {
                html += '<tr>';

                // get the id of the row
                rowId = json.rows[j]["id"];
                if (typeof rowId === 'undefined') rowId = j;

                // get the "cell" with the actual data
                cell = json.rows[j]["cell"];

                // loop over rows
                for (i = 0; i < self.ncols; i++) {
                    // get the column
                    col = self.colsmodel[i];

                    if (col.hidden != true) {
                        // get the id of the column
                        colId = col["id"];
                        if (typeof colId === 'undefined') colId = i;

                        // format cell according to colsmodel
                        classes = 'jk-table-col-' + colId + ' jk-table-row-' + rowId;

                        if (typeof col.format === 'undefined') {
                            text = cell[i];
                        } else {
                            if (col.format.type == 'filelink' && cell[i] != null) {
                                extension = cell[i].match(/(?:\.([^.]+))?$/)[1];

                                if ($.inArray(extension.toLowerCase(),['txt']) != -1) {
                                    target = 'target="_blank"';
                                } else if ($.inArray(extension.toLowerCase(),['jpg','jpeg','png','bmp']) != -1) {
                                    target = '';
                                    classes += ' jk-table-image';
                                } else {
                                    target = '';
                                }

                                classes += ' jk-table-downloadable';
                                text = '<a ' + target + 'href="' + col.format.base + '?name=' + cell[i] + '">' + cell[i] + '</a>';
                            } else if (col.format.type == 'link') {
                                text = '<a target="_blank" href="' + cell[i] + '">' + cell[i] + '</a>';
                            } else {
                                text = cell[i];
                            }
                        }

                        // add the selected class for cells in the selected column
                        if (selectedId != undefined && i == selectedId) {
                            classes += ' jk-table-col-selected';
                        }
                    
                        html += '<td class="' + classes + '">' + text + '</td>';
                    }
                }
                html += '</tr>';
            }

            // get rid of the messages
            $('.jk-table-message', this.container).children().remove();

            // get rid of the old rows
            var tbody = $('tbody',self.container)
            tbody.children().remove();

            // append the new rows to the body of the table
            tbody.append(html);
            
            // add click event for the rows (for row selection)
            $('td', self.container).click(function () {
                var element = $(this)
                var classes = element.attr('class');
                var rowClass = classes.match(/jk-table-row-\d+/)[0];

                if (self.opt.multiselect) {
                    // deselect only THIS row
                    $('.' + rowClass).removeClass('jk-table-row-selected');
                } else {
                    // deselect all rows
                    $('.jk-table-row-selected').removeClass('jk-table-row-selected');
                }

                if (classes.indexOf('jk-table-row-selected') == -1) {
                    $('.' + rowClass).addClass('jk-table-row-selected');
                }
            });

            // call the success function;
            if (typeof self.opt.success !== 'undefined') {
                self.opt.success(self);
            }
            if (typeof callback !== 'undefined') {
                callback();
            }
        }
    });
}