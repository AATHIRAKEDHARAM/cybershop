function edit_product(id) {
    console.log("test");
    var product_id = parseInt(id);
    console.log("idididid", product_id + 1)
    var formdata = new FormData();
    title = $('#title').text();
    description = $('#description').text();
    price = parseInt($('#price').text());
    quantity = parseInt($('#quantity').text());
    status = $('#status').text();
    formdata.append('id', product_id);
    formdata.append('title', title);
    formdata.append('description', description);
    formdata.append('price', price);
    formdata.append('quantity', quantity);
    formdata.append('status', status);
    console.log(typeof(price));
    console.log(description)
}