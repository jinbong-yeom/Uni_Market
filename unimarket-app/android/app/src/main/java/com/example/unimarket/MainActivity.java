package com.example.unimarket;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.fragment.app.FragmentManager;

import android.os.Bundle;
import android.view.MenuItem;
import com.google.android.material.bottomnavigation.BottomNavigationView;

public class MainActivity extends AppCompatActivity {

    Fragment1 fragment1;
//    Fragment2 fragment2;
//    Fragment3 fragment3;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        //프래그먼트생성
        fragment1 = new Fragment1();    // new 연산자 사용하더라도 바로 프래그먼트로 동작하는건 아님
//        fragment2 = new Fragment2();
//        fragment3 = new Fragment3();

        //처음엔 검색탭에서 시작
        FragmentManager fragmentManager = getSupportFragmentManager();
        fragmentManager.beginTransaction().replace(R.id.main_frame, fragment1).commit();
        BottomNavigationView bottomNavigation = findViewById(R.id.bottomNavi);

        // 하단 네비게이터 터치 시 프래그먼트 전환
        bottomNavigation.setOnItemSelectedListener(new BottomNavigationView.OnItemSelectedListener() {
            @Override
            public boolean onNavigationItemSelected(@NonNull MenuItem item) {
                switch (item.getItemId()) {
                    case R.id.search1: { //검색 탭이 선택됬을 때
                        // 프래그먼트가 이미 존재하면 보여주고 아니면 프래그먼트 매니저에 추가
                        if (fragmentManager.findFragmentByTag("search1") != null)
                            fragmentManager.beginTransaction().show(fragmentManager.findFragmentByTag("search1")).commit();
                        else
                            fragmentManager.beginTransaction().add(R.id.main_frame, new Fragment1(), "search1").commit();
                        //나머지 프래그먼트가 활성화 됬을 때 가려준다.
                        if (fragmentManager.findFragmentByTag("notice2") != null)
                            fragmentManager.beginTransaction().hide(fragmentManager.findFragmentByTag("notice2"));
                        if (fragmentManager.findFragmentByTag("setting3") != null)
                            fragmentManager.beginTransaction().hide(fragmentManager.findFragmentByTag("notice2"));
                    }
                    return true;


                    case R.id.notice2: {
                        if (fragmentManager.findFragmentByTag("notice2") != null)
                            fragmentManager.beginTransaction().show(fragmentManager.findFragmentByTag("notice2")).commit();
                        else
                            fragmentManager.beginTransaction().add(R.id.main_frame, new Fragment1(), "notice2").commit();
                        if (fragmentManager.findFragmentByTag("search1") != null)
                            fragmentManager.beginTransaction().hide(fragmentManager.findFragmentByTag("notice2"));
                        if (fragmentManager.findFragmentByTag("setting3") != null)
                            fragmentManager.beginTransaction().hide(fragmentManager.findFragmentByTag("notice2"));

                    }
                    return true;


                    case R.id.setting3: {
                        if (fragmentManager.findFragmentByTag("setting3") != null)
                            fragmentManager.beginTransaction().show(fragmentManager.findFragmentByTag("setting3")).commit();
                        else
                            fragmentManager.beginTransaction().add(R.id.main_frame, new Fragment1(), "setting3").commit();
                        if (fragmentManager.findFragmentByTag("search1") != null)
                            fragmentManager.beginTransaction().hide(fragmentManager.findFragmentByTag("notice2"));
                        if (fragmentManager.findFragmentByTag("notice2") != null)
                            fragmentManager.beginTransaction().hide(fragmentManager.findFragmentByTag("notice2"));
                    }
                    return true;

                }
                return false;
            }
        });
    }
}