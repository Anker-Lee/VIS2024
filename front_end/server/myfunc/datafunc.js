var getdata_byCode = function (model, CODE) {
    return new Promise((resolve, reject) => {
        model.find({ code: CODE }
            , {}
            , function (err, doc) {
                resolve(doc);
                return doc;
            })
    })
}

var get_Overview = function (model) {
    return new Promise((resolve, reject) => {
        model.find({}
            , { _id: 0, class: 0 }
            , function (err, doc) {
                resolve(doc);
                return doc;
            })
    })
}

var get_Ranking = function (model, industry, ratio, startTime, endTime) {
    return new Promise((resolve, reject) => {
        // model.find({"ind":{"$elemMatch":{"ind":{$in:ind},"ratio":{$gte:ratio}}}, time: {$gte :startTime, $lte : endTime}}
        //     ,{_id: 0}
        //     ,function(err,doc){
        //         resolve(doc);
        //         return doc;
        //     })

        model.aggregate([
            { $match: {  time: { $gte: startTime, $lte: endTime } } },
            {
                $group: {
                    _id: "$code",
                    // time:
                    data: {
                        $push:{
                            code : "$code",
                            date : "$time",
                            data:[
                                [
                                    {
                                        "axis":"gr",
                                        "value": "$gr"
                                    },
                                    {
                                        "axis":"egr",
                                        "value": "$egr"
                                    },
                                    {
                                        "axis":"sharpe",
                                        "value": "$sharpe"
                                    },
                                    {
                                        "axis":"beta",
                                        "value": "$beta"
                                    },
                                    {
                                        "axis":"sd",
                                        "value": "$sd"
                                    },
                                    {
                                        "axis":"ratio",
                                        "value": "$ratio"
                                    },
                                ]
                            ],
                            industry : "$ind",
                            rank: 1
                        }
                    }
                }
            },
            // { $projection: { _id: 1 } }
        ], function (err, doc) {
            //doc是全部基金经理
           doc = doc.filter(FM => {
               //FM是一个基金经理
                var flag = false;
                FM.data.forEach(oneTime => {
                    oneTime.industry.forEach(ind =>{
                        // console.log(ind)
                        // console.log(industry[0])
                        if(ind.ind == industry[0] && ind.ratio > ratio){
                            flag = true;
                            return flag;
                        }
                    })
                });
                return flag;
            })
            resolve(doc);
            
            return doc;
        })
    })
}

var get_style_byCode = function (model, Code) {
    return new Promise((resolve, reject) => {
        model.aggregate([
            { $match: { code: Code } },
            {
                $group: {
                    _id: "$code",
                    data: {
                        $push:{
                            date : "$time",
                            industry : "$ind",
                            total_percent:"$ratio",
                            return :"$gr",
                            sharpe:"$sharpe",
                            "stock_cat":[
                                { large: 6, medium: 4, small: 2, others: 1, total: 13 }
                            ]
                        }
                    }
                }
            },
        ], function (err, doc) {
            resolve(doc);
            return doc;
        })
    })
}

var get_alldata = function (model) {
    return new Promise((resolve, reject) => {
        model.find({}
            , function (err, doc) {
                resolve(doc);
                return doc;
            })
    })
}

var get_Highlight_Overview = function (model, ind, ratio, startTime, endTime) {
    return new Promise((resolve, reject) => {
        model.aggregate([
            { $match: { "ind": { "$elemMatch": { "ind": { $in: ind }, "ratio": { $gte: ratio } } }, time: { $gte: startTime, $lte: endTime } } },
            {
                $group: {
                    _id: "$code",
                    // time:
                    // data: {
                    //     $push:{
                    //         code : "$code",
                    //     }
                    // }
                }
            },
            // { $projection: { _id: 1 } }
        ], function (err, doc) {
            resolve(doc);
            return doc;
        })
    })
}

var get_Explore = function (model, ind, startTime, endTime) {
    return new Promise((resolve, reject) => {
        model.find({"ind":{$in:ind}, date: {$gte :startTime, $lte : endTime}}
            ,{_id: 0}
            ,{sort: {"date" : 1 } }
            ,function(err,doc){
                resolve(doc);
                return doc;
            })

    })
}

var get_Explore_plot = function (model, ind, startTime, endTime) {
    return new Promise((resolve, reject) => {
        console.log("ind", ind)
        console.log("startTime", startTime)
        console.log("endTime", endTime)
        model.aggregate([
            { $match: { "ind":{$in:ind}, date: { $gte: new Date(startTime) , $lte: new Date(endTime) } } },
            {
                $group: {
                    _id: "$date",
                    data: {
                        $push:{
                            code : "$code",
                            center_x : "$center_x",
                            center_y : "$center_y",
                            ind : "$ind"
                        }
                    }
                }
            },
            {
                $sort: {
                    "_id":  1
                }
            }
            // { $projection: { _id: 1 } }
        ], function (err, doc) {
            
            resolve(doc);
            
            return doc;
        })
    })
}

module.exports = {
    getdata_byCode,
    get_alldata,
    get_Overview,
    get_Ranking,
    get_Highlight_Overview,
    get_style_byCode,
    get_Explore,
    get_Explore_plot
};