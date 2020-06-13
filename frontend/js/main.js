var tree = [{
    text: "Parent1",
    nodes: [{
        text: "Child11",
        nodes: [{
            text: "GrandChild111"
        }, {
            text: "GrandChild112"
        }]
    }, {
        text: "Child12"
    }]
}, {
    text: "Parent2",
    nodes: [{
        text: "Child21"
    }, {
        text: "Child22"
    }]
}, {
    text: "Parent3",
    nodes: [{
        text: "Child31"
    }, {
        text: "Child32"
    }, {
        text: "Child33"
    }]
}, {
    text: "Parent4"
}, {
    text: "Parent5",
    nodes: [{
        text: "Child51"
    }, {
        text: "Child52"
    }, {
        text: "Child33"
    }]
}, {
    text: "Parent6"
}, {
    text: "Parent7",
    nodes: [{
        text: "Child71",
        nodes: [{
            text: "GrandChild711"
        }, {
            text: "GrandChild712"
        }]
    }, {
        text: "Child72",
        nodes: [{
            text: "GrandChild711"
        }, {
            text: "GrandChild712"
        }]
    }]
}, {
    text: "Parent8"
}, {
    text: "Parent9",
    nodes: [{
        text: "Child91"
    }, {
        text: "Child92"
    }]
}, {
    text: "Parent10"
}];


function getTree() {
    return tree;
}

$(document).ready(function () {
    var searchableTree = $('#tree').treeview({
        data: getTree(), 
        expandIcon: "fa fa-plus",
        collapseIcon: "fa fa-minus",
    });
    var inputSearch = $('#input-search');

    var search = function (e) {
        var pattern = inputSearch.val();
        var options = {
            ignoreCase: true,
            exactMatch: false,
            revealResults: true,

        };

        var results = searchableTree.treeview('search', [pattern, options]);
        console.log(results);
    }

    inputSearch.on('input', search);
});
