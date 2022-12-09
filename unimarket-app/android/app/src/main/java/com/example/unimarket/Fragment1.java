package com.example.unimarket;

import static android.content.Context.INPUT_METHOD_SERVICE;
import static java.lang.Integer.MAX_VALUE;

import android.provider.Settings.Secure;

import android.os.Bundle;
import android.provider.Settings;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.view.inputmethod.InputMethodManager;
import android.widget.Button;
import android.widget.CompoundButton;
import android.widget.EditText;
import android.widget.SearchView;
import android.widget.Switch;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.core.view.GravityCompat;
import androidx.drawerlayout.widget.DrawerLayout;
import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentManager;
import androidx.fragment.app.FragmentTransaction;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.google.android.material.floatingactionbutton.FloatingActionButton;

import com.google.android.material.navigation.NavigationView;
import com.google.android.material.snackbar.Snackbar;
import com.google.gson.JsonSyntaxException;
import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.messaging.FirebaseMessaging;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.concurrent.TimeUnit;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class Fragment1 extends Fragment {
    // 키보드를 내려주기위한 inputMethodManger 객체


    String srinput; // 검색 키워드
    String filterinput; // 필터단어
    int minprice = Integer.MAX_VALUE;
    int maxprice = 0;

    private DrawerLayout drawerLayout;
    private View drawerView;
    RecyclerView recyclerView;

    ItemAdapter adapter;
    Switch switchButton;


    public List<PostResponseData> getPostResponseData() {
        return postResponseData;
    }

    List<PostResponseData> postResponseData = new ArrayList<>();
    ArrayList<PostResponseData> temp = new ArrayList<>();    //정렬할 때 쓸 임시 리스트



    private final String BASEURL = "http://115.85.181.251:60000";


    private JsonPlaceHolderApi jsonPlaceHolderApi;

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        ViewGroup frag1V = (ViewGroup) inflater.inflate(R.layout.fragment1, container, false);
        InputMethodManager imm = (InputMethodManager) getActivity().getApplicationContext().getSystemService(INPUT_METHOD_SERVICE);



        adapter = new ItemAdapter();

        //t1 = new PostResponseData("test_title",tpic,treg,10000000,tdes,appname,ttime,tseller);

        Retrofit retrofit = new Retrofit.Builder()
                .baseUrl(BASEURL)
                .addConverterFactory(GsonConverterFactory.create())
                .build();

        jsonPlaceHolderApi = retrofit.create(JsonPlaceHolderApi.class);

        SearchView searchBar = frag1V.findViewById(R.id.searchView1);
        searchBar.bringToFront();   // 뷰 상단으로 올리기(드러워가 겹쳐도 터치 되도록)
        searchBar.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                searchBar.setIconified(false); //전체영역 터치되도록(원래 아이콘영역만됬음)
            }
        });
        searchBar.setOnQueryTextListener(new SearchView.OnQueryTextListener() {
            @Override
            public boolean onQueryTextSubmit(String s) { // 검색 눌렀을 때
//                if (((Globalstr) getActivity().getApplication() ).getregion1()==null){
//                    Snackbar.make(frag1V,"지역을 추가해주세요", Snackbar.LENGTH_SHORT).show();
//                    return true;
//                }

                srinput = s;
                Toast.makeText(getActivity(),s+"입력", Toast.LENGTH_SHORT).show();

                if(postResponseData != null){
                    postResponseData = new ArrayList<>();
                }
                createPost(s);
//                if(postResponseData != null){
//                    temp = adapter.getItems();
//                }


//                for (PostResponseData f : postResponseData) {
//                    try {
//                        temp.add(f.clone());
//                    } catch (CloneNotSupportedException e) {
//                        e.printStackTrace();
//                    }
//                }






                // 받아온 상품
//                for (int i = 0; i < postResponseData.size(); i++) {
//                    PostResponseData tmpResponseData = postResponseData.get(i);
//                    adapter.addItem(tmpResponseData);
//                }
//                for (int i = 0; i < 10; i++) {      //test
//                    //PostResponseData tmpResponseData = postResponseData.get(i);
//                    adapterd.addItem(t1);
//                }
//                postResponseData.clear();
//                adapter.notifyDataSetChanged();

    



                // 입력받은 문자열 처리
                frag1V.bringChildToFront(recyclerView); //리사이클러 위로 올리기
                searchBar.clearFocus(); //에딧 텍스트 포커스를 제거
                imm.hideSoftInputFromWindow(searchBar.getWindowToken(), 0);
                return true;    //액션을 listener 로 handle 하는 경우  true 를 준다,

            }
            @Override
            public boolean onQueryTextChange(String s) {
                // 입력란의 문자열이 바뀔 때 처리
                //Toast.makeText(getActivity(), "입력값 수정", Toast.LENGTH_LONG).show();
                return false;
            }
        });

        FloatingActionButton snbutton = frag1V.findViewById(R.id.floatingActionButton);
        snbutton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                //알림 설정하는 파트
                createNotice(srinput);

                // 번들 생성하여 검색어 fragment2에 넘기기
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
        filter.setOnClickListener(new View.OnClickListener() { // 필터 레이아웃(드로어)펼치기
            @Override
            public void onClick(View view) {
                frag1V.bringChildToFront(drawerLayout); //리사이클러때문에 터치안되는거 방지
                Toast.makeText(getActivity(), "필터클릭", Toast.LENGTH_SHORT).show();
                drawerLayout.openDrawer(drawerView);
            }
        });
        drawerLayout = (DrawerLayout) frag1V.findViewById(R.id.drawer);
        drawerView = (View) frag1V.findViewById(R.id.drawerView);
        drawerLayout.addDrawerListener(listener);   //setDrawerListener deprecated

        EditText filterv = frag1V.findViewById(R.id.filter_et1);
        EditText minv = frag1V.findViewById(R.id.filter_et2);
        EditText maxv = frag1V.findViewById(R.id.filter_et3);

        Button filterb = frag1V.findViewById(R.id.filter_button1);
        filterb.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                //Toast.makeText(getActivity(),"적용버튼 클릭", Toast.LENGTH_LONG).show();
                filterinput = filterv.getText().toString();
                minprice = Integer.parseInt(minv.getText().toString());
                maxprice = Integer.parseInt(maxv.getText().toString());
                Toast.makeText(getActivity(),filterinput+minprice+maxprice, Toast.LENGTH_LONG).show();
                // 필터 적용 됐을 때 출력내용 바뀌거나 필터 값 전송되도록 ++++++++++++++++++++++++++++++++

            }
        });

        recyclerView = frag1V.findViewById(R.id.recycler);
        LinearLayoutManager layoutManager = new LinearLayoutManager(getActivity(), LinearLayoutManager.VERTICAL, false);
        recyclerView.setLayoutManager(layoutManager);
        recyclerView.setAdapter(adapter);

        // 스위치 버튼 눌렀을 때 정렬 방식 변경
        switchButton = frag1V.findViewById(R.id.switch1);
        switchButton.bringToFront();
        switchButton.setOnCheckedChangeListener(new Switch.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
                // 스위치 버튼이 체크되었는지 검사하여 텍스트뷰에 각 경우에 맞게 출력합니다.
                if (isChecked){
                    switchButton.setText("시간정렬");
                    adapter.setItems(adapter.SortedToTime());
                    adapter.notifyDataSetChanged();

                }else{
                    switchButton.setText("가격정렬");
                    createPost(srinput);
                    adapter.notifyDataSetChanged();
                }
            }
        });

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




    private void createPost(String s) {
        String android_id =Settings.Secure.getString(getContext().getContentResolver(), Secure.ANDROID_ID);

        List<String> excludeKeyword = new ArrayList<>();
        List<String> region = new ArrayList<>();

//        excludeKeyword.add(filterinput);
//        int max_price = maxprice;
//        int min_price = minprice;
//        region.add(((Globalstr) getActivity().getApplication() ).getregion1());

        excludeKeyword.add("가위");       //test
        region.add("청주");


        //FilteringData filteringData = new FilteringData(excludeKeyword, max_price, min_price, region);
        FilteringData filteringData = new FilteringData(excludeKeyword, MAX_VALUE, 0, region);  //test


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
                adapter.clear();


                postResponseData.addAll(0, postResponse.getResult());

                //시간 순으로 정렬
                //PostResponse tmpResponse = new PostResponse(postResponseData);
                //postResponseData = tmpResponse.SortedToTime();
                //
                for(int i = 0; i< postResponseData.size();i++) {
                    PostResponseData tmpResponseData = postResponseData.get(i);
                    adapter.addItem(tmpResponseData);


                }
                postResponseData.clear();
                adapter.notifyDataSetChanged();
            }
            @Override
            public void onFailure(Call<PostResponse> call, Throwable t) {
                Toast.makeText(getActivity(), "없다.", Toast.LENGTH_SHORT).show();
            }
        });
    }

    private void createNotice(String s) {
        String token = new String();
        //파이어베이스 토큰확인
        try {
            srinput = s;
            Task<String> task = FirebaseMessaging.getInstance().getToken();
            while (!task.isSuccessful());
            token = task.getResult();

        } catch (Exception e) {
            e.printStackTrace();
        }

        //필터링 정보 만들기
        List<String> excludeKeyword = new ArrayList<>();
        List<String> region = new ArrayList<>();
        excludeKeyword.add(filterinput);
        Globalstr globalstr = new Globalstr();
        region.add(globalstr.getregion1());


        FilteringData filteringData = new FilteringData(excludeKeyword, maxprice, minprice, region);

        send(s, token, filteringData);
    }

    public void send(String s, String token, FilteringData filteringData){
        String user_id = Settings.Secure.getString(getContext().getContentResolver(), Secure.ANDROID_ID);
        Boolean send = true;
        NoticeData noticeData = new NoticeData(s, user_id, token, filteringData, send);


        Call<NoticeResponse> call = jsonPlaceHolderApi.createNotice(noticeData);
        call.enqueue(new Callback<NoticeResponse>() {
            @Override
            public void onResponse(Call<NoticeResponse> call, Response<NoticeResponse> response) {
                if (!response.isSuccessful()) {
                    Toast.makeText(getActivity(),s, Toast.LENGTH_SHORT).show();
                    return;
                }
                Toast.makeText(getActivity(),s, Toast.LENGTH_SHORT).show();
                NoticeResponse noticeResponse = response.body();

            }


            @Override
            public void onFailure(Call<NoticeResponse> call, Throwable t) {
                t.printStackTrace();
                Toast.makeText(getActivity(), "오류", Toast.LENGTH_SHORT).show();
            }
        });
    }


}
