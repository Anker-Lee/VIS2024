const mongoose = require('mongoose');
const url = "mongodb://47.103.198.236/jsonVee2"

mongoose.connect(url,{useNewUrlParser: true, useUnifiedTopology: true })
.then(res =>{
    res && console.log('connection success');
}).catch(err=>{
    err && console.log('connection failed')
});

const selecting_timeSchema = new mongoose.Schema({
    _id: {type: String},
    type: {type: String},
    date: {type: Date},
    value: {type: Number}
})

const selecting_countSchema = new mongoose.Schema({
    _id: {type: String},
    ind: {type: String},
    date: {type: Date},
    count: {type: Number}
})

const explore_rankingSchema = new mongoose.Schema({
    _id: {type: String},
    ind: {type: String},
    date: {type: Date},
    data: [{
        _id : {type: String},
        data:[{
            code : {type: String},
            name : {type: String},
            date : {type: String},
            gr : {type: Number},
            egr : {type: Number},
            sharpe : {type: Number},
            beta : {type: Number},
            sd : {type: Number},
            ind :[{
                ind: {type: String},
                ratio:{type: Number}
            }]
        }]
    }]
})

const explore_plotSchema = new mongoose.Schema({
    _id: {type: String},
    ind: {type: String},
    date: {type: Date},
    code :{type: String},
    center_x: {type: Number},
    center_y: {type: Number}
})


const SelectingTimeModel = mongoose.model('selecing_time_model',selecting_timeSchema,'time');
const SelectingCountModel = mongoose.model('selecting_count_model',selecting_countSchema,'count');
const ExploreRankingModel = mongoose.model('explore_ranking_model',explore_rankingSchema,'ranking');
const ExploreOveriewModel = mongoose.model('explore_overview_model',explore_plotSchema,'overview');

module.exports = {
    SelectingTimeModel,
    SelectingCountModel,
    ExploreRankingModel,
    ExploreOveriewModel,
}