package com.example.unimarket;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.fragment.app.FragmentManager;

import android.content.Context;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.view.MenuItem;
import android.widget.Toast;

import com.google.android.material.bottomnavigation.BottomNavigationView;

public class MainActivity extends AppCompatActivity {

     Fragment1 fragment1;
     Fragment2 fragment2;
     Fragment3 fragment3;
     FragmentManager fragmentManager = getSupportFragmentManager();
     public static Context context;


    public void makefrag2(){
        fragment2 = new Fragment2();
        fragmentManager.beginTransaction().add(R.id.main_frame, fragment2).commit();
        Toast.makeText(getApplicationContext(), "make frag2", Toast.LENGTH_LONG).show();
    }
    public void removefrag2() {
        if (fragment2 != null) {
            fragmentManager.beginTransaction().remove(fragment2).commit();
            Toast.makeText(getApplicationContext(), "removefrag2", Toast.LENGTH_LONG).show();
        }
    }
    public void gohistory() {
        Intent intent = new Intent(Intent.ACTION_VIEW, Uri.parse(getString(R.string.app_history)));
        startActivity(intent);
    }
    public void goToItem(String link) {
        Intent intent = new Intent(Intent.ACTION_VIEW, Uri.parse(link));
        startActivity(intent);
    }


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        context = this;


        //프래그먼트생성
        fragment1 = new Fragment1();    // new 연산자 사용하더라도 바로 프래그먼트로 동작하는건 아님
        //fragment2 = new Fragment2();
//        fragment3 = new Fragment3();

        //처음엔 검색탭에서 시작
        //FragmentManager fragmentManager = getSupportFragmentManager();
        fragmentManager.beginTransaction().replace(R.id.main_frame, fragment1).commit();
        BottomNavigationView bottomNavigation = findViewById(R.id.bottomNavi);

        // 하단 네비게이터 터치 시 프래그먼트 전환
        bottomNavigation.setOnItemSelectedListener(new BottomNavigationView.OnItemSelectedListener() {
            @Override
            public boolean onNavigationItemSelected(@NonNull MenuItem item) {
                switch (item.getItemId()) {
                    case R.id.search1: { //검색 탭이 선택됬을 때
                        // 프래그먼트가 이미 존재하면 보여주고 아니면 프래그먼트 매니저에 추가
                        if (fragment1 == null) {
                            fragment1 = new Fragment1();
                            fragmentManager.beginTransaction().add(R.id.main_frame, fragment1).commit();
                            Toast.makeText(getApplicationContext(), "frag1add", Toast.LENGTH_LONG).show();
                        }
                        if (fragment1 != null) fragmentManager.beginTransaction().show(fragment1).commit();

                        //나머지 프래그먼트가 활성화 됬을 때 가려준다.
                        if (fragment2 != null) fragmentManager.beginTransaction().hide(fragment2).commit();
                        if (fragment3 != null) fragmentManager.beginTransaction().hide(fragment3).commit();

                        return true;
                    }

                    case R.id.notice2: {
                        if (fragment2 == null) {
                            fragment2 = new Fragment2();
                            fragmentManager.beginTransaction().add(R.id.main_frame, fragment2).commit();
                            Toast.makeText(getApplicationContext(), "frag2add", Toast.LENGTH_LONG).show();
                        }
                        if (fragment2 != null) fragmentManager.beginTransaction().show(fragment2).commit();

                        if (fragment1 != null) fragmentManager.beginTransaction().hide(fragment1).commit();
                        if (fragment3 != null) fragmentManager.beginTransaction().hide(fragment3).commit();

                        return true;
                    }


                    case R.id.setting3: {
                        if (fragment3 == null) {
                            fragment3 = new Fragment3();
                            fragmentManager.beginTransaction().add(R.id.main_frame, fragment3).commit();
                            Toast.makeText(getApplicationContext(), "frag3add", Toast.LENGTH_LONG).show();
                        }
                        if (fragment3 != null) fragmentManager.beginTransaction().show(fragment3).commit();

                        if (fragment1 != null) fragmentManager.beginTransaction().hide(fragment1).commit();
                        if (fragment2 != null) fragmentManager.beginTransaction().hide(fragment2).commit();

                        return true;
                    }
                    default:return false;
                }
            }
        });
    }
}