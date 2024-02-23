const mongoose = require('mongoose');
const url = "mongodb://47.103.198.236/jsonVee"

mongoose.connect(url,{useNewUrlParser: true, useUnifiedTopology: true })
.then(res =>{
    res && console.log('connection success');
}).catch(err=>{
    err && console.log('connection failed')
});

const overviewSchema = new mongoose.Schema({
    _id: {type: String},
    code: {type: String},
    center_x: {type: Number},
    center_y: {type: Number},
    class: {type: Number}
})

const rankingSchema = new mongoose.Schema({
    _id: {type: String},
    time:{type: Number},
    code: {type: String},
    fm:{type: String},
    abbr:{type: String},
    education:{type: String},
    gender:{type: String},
    work_years:{type: Number},
    awards:{type: Number},
    ind:[
        {"ind":{type: String}},
        {"ratio":{type: Number}},
    ],
    gr:{type: Number},
    egr:{type: Number},
    sharpe:{type: Number},
    beta:{type: Number},
    sd:{type: Number},
    ratio:{type: Number},
})

const timeSchema = new mongoose.Schema({
    _id: {type: String},
    type: {type: String},
    date: {type: Date},
    value: {type: String}
})

const OverviewModel = mongoose.model('overviewmodel',overviewSchema,'overview');
const RankingModel = mongoose.model('rankingmodel',rankingSchema,'ranking');
const TimeModel = mongoose.model('timemodel', timeSchema, 'time')

module.exports = {
    OverviewModel,
    RankingModel,
    TimeModel,
}