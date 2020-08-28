const gridOptions = {

    rowModelType: 'serverSide',
    pagination: true,
    paginationPageSize: 10,
    cacheBlockSize: 10,

    columnDefs: [
        {field: 'athlete'},
        {field: 'gold', aggFunc: 'sum'},
        {field: 'silver', aggFunc: 'sum'},
        {field: 'bronze', aggFunc: 'sum'},
    ],

    defaultColDef: {
        sortable: true
    },

    debug: true,
};


var gridDiv = document.querySelector('#myGrid');
new agGrid.Grid(gridDiv, gridOptions);

const datasource = {
    /*
        gridでデータ取得の操作をすると呼ばれる
     */
    getRows(params) {
        console.log(JSON.stringify(params.request, null, 1));

        fetch("http://localhost:9000/items/" + params.request.startRow,
            {
                method: "GET", // *GET, POST, PUT, DELETE, etc.
                mode: "cors", // no-cors, cors, *same-origin
                cache: "no-cache", // *default, no-cache, reload, force-cache, only-if-cached
                headers: {"Accept": "application/json"}
            }
        )
            .then((httpResponse) => {
                if (!httpResponse.ok) {
                    throw new Error();
                }
                return httpResponse.json();
            })

            .then(response => {
                console.log(response);
                console.log(response.rows);
                params.successCallback(response.rows, response.lastRow);
            })
            .catch(error => {
                console.error(error);
                params.failCallback();
            })
    }
};

gridOptions.api.setServerSideDatasource(datasource);