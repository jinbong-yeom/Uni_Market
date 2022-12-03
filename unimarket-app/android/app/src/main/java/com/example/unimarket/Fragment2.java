package com.example.unimarket;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.fragment.app.Fragment;

public class Fragment2 extends Fragment {
    String trans;   // frag1에서 넘겨받은 값

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        ViewGroup frag3V = (ViewGroup) inflater.inflate(R.layout.fragment3, container, false);

        return frag3V;
    }

}
