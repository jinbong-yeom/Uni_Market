package com.example.unimarket;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import androidx.fragment.app.Fragment;

public class Fragment3 extends Fragment {
    String regstr;

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        ViewGroup frag3V = (ViewGroup) inflater.inflate(R.layout.fragment3, container, false);

        EditText reginput = frag3V.findViewById(R.id.reg_input);
        Button button1 = frag3V.findViewById(R.id.regionplus);
        TextView regshow = frag3V.findViewById(R.id.regshow);

        button1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                regstr = reginput.getText().toString();
                //Toast.makeText(getActivity(),regstr, Toast.LENGTH_LONG).show();
                regshow.setText(regstr);

                ( (Globalstr) getActivity().getApplication() ).setregion1(regstr);
                //Toast.makeText(getActivity(),( (Globalstr) getActivity().getApplication() ).getregion1(), Toast.LENGTH_LONG).show();
            }
        });

        Button email = frag3V.findViewById(R.id.report);
        email.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Toast.makeText(getActivity(),"이메일 버튼 눌림", Toast.LENGTH_SHORT).show();

            }
        });



        return frag3V;
    }

}
