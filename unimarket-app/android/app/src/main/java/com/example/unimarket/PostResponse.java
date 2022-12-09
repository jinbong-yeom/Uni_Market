package com.example.unimarket;

import com.google.gson.annotations.SerializedName;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class PostResponse {
    @SerializedName("result")
    private List<PostResponseData> result;
    private List<PostResponseData> replaceResult;


    public PostResponse(List<PostResponseData> result) {
        this.result = result;
    }

    public List<PostResponseData> getResult() {
        return result;
    }


    public List<PostResponseData> SortedToTime(){
        this.replaceResult = result;
        List<PostResponseData> sortedData = this.result;
        Collections.sort(sortedData);

        return sortedData;
    }

    public List<PostResponseData> ReplaceSorting(){
        List<PostResponseData> temp = result;
        this.result = replaceResult;
        this.replaceResult = temp;

        return result;
    }




}
