package com.example.unimarket;

import static java.lang.Integer.MAX_VALUE;

import android.os.Bundle;
import android.provider.Settings;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import androidx.fragment.app.Fragment;

import java.util.ArrayList;
import java.util.List;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class Fragment2 extends Fragment {
    String trans;   // frag1에서 넘겨받은 값

    private JsonPlaceHolderApi jsonPlaceHolderApi;

    private final String BASEURL = "http://115.85.181.251:60000";
    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        ViewGroup frag2V = (ViewGroup) inflater.inflate(R.layout.fragment2, container, false);
        TextView nkeyword = frag2V.findViewById(R.id.frag2_textView2);

        Retrofit retrofit = new Retrofit.Builder()
                .baseUrl(BASEURL)
                .addConverterFactory(GsonConverterFactory.create())
                .build();

        jsonPlaceHolderApi = retrofit.create(JsonPlaceHolderApi.class);


        if (getArguments() != null) {
            trans = getArguments().getString("srinput"); // 프래그먼트1에서 받아온 값 넣기
            //Toast.makeText(getActivity(),trans +"넘겨받은 문자열", Toast.LENGTH_LONG).show();
            nkeyword.setText(trans);
        }

        Button resetreg = frag2V.findViewById(R.id.button2);
        resetreg.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                deleteNotice();
                Toast.makeText(getActivity(),trans +"넘겨받은 문자열", Toast.LENGTH_LONG).show();

            }
        });


        return frag2V;
    }

    private void deleteNotice() {
        String user_id =Settings.Secure.getString(getContext().getContentResolver(), Settings.Secure.ANDROID_ID);
        DeleteData  deleteData = new DeleteData(user_id);
        Call<DeleteResponse> call = jsonPlaceHolderApi.deleteNotice(deleteData);
        call.enqueue(new Callback<DeleteResponse>() {
            @Override
            public void onResponse(Call<DeleteResponse> call, Response<DeleteResponse> response) {
                if (!response.isSuccessful()) {
                    return;
                }
                DeleteResponse deleteResponse = response.body();

            }

            @Override
            public void onFailure(Call<DeleteResponse> call, Throwable t) {
                t.printStackTrace();
                Toast.makeText(getActivity(), "오류", Toast.LENGTH_SHORT).show();
            }
        });
    }

}
