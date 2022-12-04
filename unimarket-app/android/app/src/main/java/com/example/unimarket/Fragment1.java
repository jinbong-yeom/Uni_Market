package com.example.unimarket;

import android.provider.Settings.Secure;

import android.os.Bundle;
import android.provider.Settings;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.SearchView;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.fragment.app.Fragment;

import com.google.gson.JsonSyntaxException;
import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.messaging.FirebaseMessaging;

import java.util.ArrayList;
import java.util.List;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class Fragment1 extends Fragment {

    private final String BASEURL = "http://115.85.181.251:60000";

    private JsonPlaceHolderApi jsonPlaceHolderApi;

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        ViewGroup frag1V = (ViewGroup) inflater.inflate(R.layout.fragment1, container, false);

        Retrofit retrofit = new Retrofit.Builder()
                .baseUrl(BASEURL)
                .addConverterFactory(GsonConverterFactory.create())
                .build();

        jsonPlaceHolderApi = retrofit.create(JsonPlaceHolderApi.class);



        SearchView searchBar = frag1V.findViewById(R.id.searchView1);
        searchBar.setOnQueryTextListener(new SearchView.OnQueryTextListener() {
            @Override
            public boolean onQueryTextSubmit(String s) {
                createPost(s);
                createNotice(s);
                // 입력받은 문자열 처리
//                Toast.makeText(getActivity(),s, Toast.LENGTH_SHORT).show();
                return true;    //리스너로 처리할 떄 true반환?
            }
            @Override
            public boolean onQueryTextChange(String s) {
                // 입력란의 문자열이 바뀔 때 처리
                //Toast.makeText(getActivity(), "입력값 수정", Toast.LENGTH_LONG).show();
                return false;
            }


            private void createPost(String s) {
                String android_id =Settings.Secure.getString(getContext().getContentResolver(), Secure.ANDROID_ID);
                List<String> region = new ArrayList<>();
                region.add("청주");
                region.add("서울");
                PostData postData = new PostData(s, android_id, region);

                Call<PostResponse> call = jsonPlaceHolderApi.createPost(postData);

                call.enqueue(new Callback<PostResponse>() {

                    @Override
                    public void onResponse(Call<PostResponse> call, Response<PostResponse> response) {
                        if (!response.isSuccessful()) {
                            Toast.makeText(getActivity(),"없음", Toast.LENGTH_SHORT).show();
                            return;
                        }
                        PostResponse postResponse = response.body();
                        Toast.makeText(getActivity(),postResponse.getResult().get(0).getTitle(), Toast.LENGTH_SHORT).show();
                    }
                    @Override
                    public void onFailure(Call<PostResponse> call, Throwable t) {
                        Toast.makeText(getActivity(), "없다.", Toast.LENGTH_SHORT).show();
                    }
                });
            }

            private void createNotice(String s) {
                //파이어베이스 토큰확인
                String token = FirebaseMessaging.getInstance().getToken().getResult();
                Toast.makeText(getActivity(),token, Toast.LENGTH_SHORT).show();
                send(s, token);
            }

            public void send(String s, String token){
                List<String> region = new ArrayList<>();
                region.add("청주");
                region.add("서울");

                PostData postData = new PostData(s, token, region);


                Call<NoticeResponse> call = jsonPlaceHolderApi.createNotice(postData);

                call.enqueue(new Callback<NoticeResponse>() {
                    @Override
                    public void onResponse(Call<NoticeResponse> call, Response<NoticeResponse> response) {
                        if (!response.isSuccessful()) {
                            Toast.makeText(getActivity(),s, Toast.LENGTH_SHORT).show();
                            return;
                        }
                        NoticeResponse postResponse = response.body();
                    }


                    @Override
                    public void onFailure(Call<NoticeResponse> call, Throwable t) {
                        t.printStackTrace();
                        Toast.makeText(getActivity(), "오류", Toast.LENGTH_SHORT).show();
                    }
                });
            }
        });



        return frag1V;
    }



}
