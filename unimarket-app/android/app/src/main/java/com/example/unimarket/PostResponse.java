package com.example.unimarket;

import com.google.gson.annotations.SerializedName;

import java.util.List;

public class PostResponse {
    @SerializedName("result")
    private List<PostResponseData> result;

    public PostResponse(List<PostResponseData> result) {
        this.result = result;
    }

    public List<PostResponseData> getResult() {
        return result;
    }
}
