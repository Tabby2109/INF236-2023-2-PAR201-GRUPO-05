const { Schema, model } = require('mongoose')


const radiografiaSchema = new Schema({
    rut : Number,
    email : String,
    fecha : Date,
    nombre : String,
    hora : Date,
    random : String,
    

})

module.exports = model('radiografia',radiografiaSchema)