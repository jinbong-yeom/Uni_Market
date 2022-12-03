package com.example.unimarket;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.fragment.app.FragmentManager;

import android.os.Bundle;
import android.view.MenuItem;
import com.google.android.material.bottomnavigation.BottomNavigationView;

public class MainActivity extends AppCompatActivity {

    Fragment1 fragment1;
    Fragment2 fragment2;
    Fragment3 fragment3;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        //프래그먼트생성
        fragment1 = new Fragment1();    // new 연산자 사용하더라도 바로 프래그먼트로 동작하는건 아님
        fragment2 = new Fragment2();
        fragment3 = new Fragment3();

        //처음엔 검색탭에서 시작
        FragmentManager fragmentManager = getSupportFragmentManager();
        fragmentManager.beginTransaction().replace(R.id.main_frame, fragment1).commit();
        BottomNavigationView bottomNavigation = findViewById(R.id.bottomNavi);

        // 하단 네비게이터 터치 시 프래그먼트 전환
        bottomNavigation.setOnItemSelectedListener(new BottomNavigationView.OnItemSelectedListener() {
            @Override
            public boolean onNavigationItemSelected(@NonNull MenuItem item) {
                switch (item.getItemId()) {
                    case R.id.search1:
                            fragmentManager.beginTransaction()
                                .replace(R.id.main_frame, fragment1).commit();
                        return true;
                    case R.id.notice2:
                        fragmentManager.beginTransaction()
                                .replace(R.id.main_frame, fragment2).commit();
                        return true;
                    case R.id.setting3:
                        fragmentManager.beginTransaction()
                                .replace(R.id.main_frame, fragment3).commit();
                        return true;
                }
                return false;
            }
        });
    }
}