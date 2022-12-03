package com.example.unimarket;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;

import androidx.fragment.app.Fragment;

public class Fragment3 extends Fragment {
    String regstr;

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        ViewGroup frag3V = (ViewGroup) inflater.inflate(R.layout.fragment3, container, false);

        Button button1 = frag3V.findViewById(R.id.regionplus);



        return frag3V;
    }

}
