package com.example.unimarket;

import android.animation.ValueAnimator;
import android.content.Context;
import android.util.SparseBooleanArray;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.constraintlayout.widget.ConstraintLayout;
import androidx.recyclerview.widget.RecyclerView;

import com.bumptech.glide.Glide;

import java.text.DecimalFormat;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

// 검색해서 받아온 상품 item.xml이랑 매칭
public class ItemAdapter extends RecyclerView.Adapter<RecyclerView.ViewHolder> {
    ArrayList<PostResponseData> items = new ArrayList<PostResponseData>();

    // Item의 클릭 상태를 저장할 array 객체
    private SparseBooleanArray selectedItems = new SparseBooleanArray();
    // 직전에 클릭됐던 Item의 position
    private int prePosition = -1;

    //private Context context;


    @NonNull
    @Override
    public RecyclerView.ViewHolder onCreateViewHolder(@NonNull ViewGroup viewGroup, int viewType) { //뷰홀더가 만들어질 때
        LayoutInflater inflater = LayoutInflater.from(viewGroup.getContext());
        View itemView = inflater.inflate(R.layout.item, viewGroup, false);

//        View itemView = LayoutInflater.from(viewGroup.getContext()).inflate(R.layout.item, viewGroup, false);
        return new ViewHolderItem(itemView);
    }

    @Override
    public void onBindViewHolder(@NonNull RecyclerView.ViewHolder holder, int position) { //인덱스에 맞는 객체를 찾음
        PostResponseData item = items.get(position);
        //holder.setItem(item);

        ViewHolderItem viewholderitem = (ViewHolderItem)holder;
        viewholderitem.setItem(items.get(position),position, selectedItems);
        viewholderitem.setOnViewHolderItemClickListener(new OnViewHolderItemClickListener() {
            @Override
            public void onViewHolderItemClick() {
                if (selectedItems.get(position)) {
                    // 펼쳐진 Item을 클릭 시
                    selectedItems.delete(position);
                } else {
                    // 직전의 클릭됐던 Item의 클릭상태를 지움
                    selectedItems.delete(prePosition);
                    // 클릭한 Item의 position을 저장
                    selectedItems.put(position, true);
                }
                // 해당 포지션의 변화를 알림
                if (prePosition != -1) notifyItemChanged(prePosition);
                notifyItemChanged(position);
                // 클릭된 position 저장
                prePosition = position;
            }
        });

    }
    // 받아온 상품 수
    @Override
    public int getItemCount() {
        return items.size();
    }
    //리스트에 아이템 추가
    public void addItem(PostResponseData item) {
        items.add(item);
    }

    public void setItems(ArrayList<PostResponseData> items) {
        this.items = items;
    }

    public PostResponseData getItem(int position) {
        return items.get(position);
    }


    // 원래 뷰 삭제
    public void clear() {
        this.items.clear();
    }


    //시간 순 정렬
    public ArrayList<PostResponseData> SortedToTime(){
        ArrayList<PostResponseData> sortedData = this.items;
        Collections.sort(sortedData);

        return sortedData;
    }
}
