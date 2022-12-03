package com.example.unimarket;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import androidx.fragment.app.Fragment;

public class Fragment2 extends Fragment {
    String trans;   // frag1에서 넘겨받은 값

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        ViewGroup frag2V = (ViewGroup) inflater.inflate(R.layout.fragment3, container, false);
        TextView nkeyword = frag2V.findViewById(R.id.frag2_textView2);

        if (getArguments() != null) {
            trans = getArguments().getString("srinput"); // 프래그먼트1에서 받아온 값 넣기
            //Toast.makeText(getActivity(),trans +"넘겨받은 문자열", Toast.LENGTH_LONG).show();
            nkeyword.setText(trans);
        }

        return frag2V;
    }
}
