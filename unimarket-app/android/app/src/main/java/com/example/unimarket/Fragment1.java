package com.example.unimarket;

import android.provider.Settings.Secure;

import android.os.Bundle;
import android.provider.Settings;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.EditText;
import android.widget.SearchView;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.core.view.GravityCompat;
import androidx.drawerlayout.widget.DrawerLayout;
import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentManager;
import androidx.fragment.app.FragmentTransaction;

import com.google.android.material.floatingactionbutton.FloatingActionButton;

import com.google.android.material.navigation.NavigationView;
import com.google.gson.JsonSyntaxException;

import java.util.ArrayList;
import java.util.List;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class Fragment1 extends Fragment {

    String srinput; // 검색 키워드드
    private DrawerLayout drawerLayout;
    private View drawerView;

    private final String BASEURL = "http://172.27.0.194:60000";

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
                srinput = s;
                //createPost(s);
                // 입력받은 문자열 처리
                Toast.makeText(getActivity(),s+"입력", Toast.LENGTH_SHORT).show();
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
                List<String> test =  new ArrayList<>();
                test.add("note");
                test.add("book");
                List<String> test1 = new ArrayList<>();
                test1.add("청주");
                FilteringData filteringData = new FilteringData(test, 1500000, 500000, test1);
                PostData postData = new PostData(s, android_id, filteringData);


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
        });

        FloatingActionButton snbutton = frag1V.findViewById(R.id.floatingActionButton);
        snbutton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                //Toast.makeText(getActivity(),srinput +" fragment2로 전송", Toast.LENGTH_LONG).show();

                //알림 설정하는 파트

                // 번들 생성하여 검색어 fragment2에 넘기기 -  강제이동안되도록 수정 필요
                Bundle bundle = new Bundle();
                bundle.putString("srinput",srinput);

                FragmentManager fragmentManager = getActivity().getSupportFragmentManager();
                Fragment1 fragment1 = ((MainActivity)getActivity()).fragment1;
                Fragment2 fragment2 = ((MainActivity)getActivity()).fragment2;

                if (fragment2!=null) {
                    ((MainActivity)getActivity()).removefrag2();
                }
                ((MainActivity)getActivity()).makefrag2();
                fragment2 = ((MainActivity)getActivity()).fragment2;
                fragment2.setArguments(bundle); //번들을 프래그먼트2로 보냄

                // 알림 탭으로 이동
                fragmentManager.beginTransaction().hide(fragment1).commit();
                fragmentManager.beginTransaction().show(fragment2).commit();
            }
        });

        Button filter = frag1V.findViewById(R.id.filter);
        filter.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Toast.makeText(getActivity(), "필터클릭", Toast.LENGTH_SHORT).show();
                drawerLayout.openDrawer(drawerView);
            }
        });
        drawerLayout = (DrawerLayout) frag1V.findViewById(R.id.drawer);
        drawerView = (View) frag1V.findViewById(R.id.drawerView);
        drawerLayout.addDrawerListener(listener);;   //setDrawerListener deprecated

        EditText filterv = frag1V.findViewById(R.id.filter_et1);
        EditText minv = frag1V.findViewById(R.id.filter_et2);
        EditText maxv = frag1V.findViewById(R.id.filter_et3);



        return frag1V;
    }
    DrawerLayout.DrawerListener listener = new DrawerLayout.DrawerListener() {
        @Override
        public void onDrawerSlide(@NonNull View drawerView, float slideOffset) {
        }

        @Override
        public void onDrawerOpened(@NonNull View drawerView) {
        }

        @Override
        public void onDrawerClosed(@NonNull View drawerView) {
        }

        @Override
        public void onDrawerStateChanged(int newState) {
        }
    };




}
