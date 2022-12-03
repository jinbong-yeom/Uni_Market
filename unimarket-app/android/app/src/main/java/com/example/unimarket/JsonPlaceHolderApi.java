package com.example.unimarket;

import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.POST;

public interface JsonPlaceHolderApi {

    @POST("post")
    Call<PostResponse> createPost(@Body PostData postData);

}
