const mongoose = require('mongoose')
const database = "holder";

mongoose.connect(`mongodb://localhost/${database}`, {
    useNewUrlParser: true,
    useUnifiedTopology: true
}) 
    .then(res => console.log('CONNECTED'))
    .catch(err => console.log(`FAILED TO CONNECT........${err}`))

