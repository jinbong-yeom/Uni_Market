package com.example.unimarket;

import android.animation.ValueAnimator;
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
// 검색해서 받아온 상품 item.xml이랑 매칭
public class ItemAdapter extends RecyclerView.Adapter<ItemAdapter.ViewHolder> {
    ArrayList<PostResponseData> items = new ArrayList<PostResponseData>();

    // Item의 클릭 상태를 저장할 array 객체
    private SparseBooleanArray selectedItems = new SparseBooleanArray();
    // 직전에 클릭됐던 Item의 position
    private int prePosition = -1;


    @NonNull
    @Override
    public ViewHolder onCreateViewHolder(@NonNull ViewGroup viewGroup, int viewType) { //뷰홀더가 만들어질 때
        LayoutInflater inflater = LayoutInflater.from(viewGroup.getContext());
        View itemView = inflater.inflate(R.layout.item, viewGroup, false);

        return new ViewHolder(itemView);
    }

    @Override
    public void onBindViewHolder(@NonNull ViewHolder viewHolder, int position) { //인덱스에 맞는 객체를 찾음
        PostResponseData item = items.get(position);
        //viewHolder.setItem(item);

        ViewHolder viewHolderItem = (ViewHolder)viewHolder;
        viewHolderItem.setItem(items.get(position),position, selectedItems);
        viewHolderItem.setOnViewHolderItemClickListener(new OnViewHolderItemClickListener() {
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

    public class ViewHolder extends RecyclerView.ViewHolder {
        TextView titleView;
        TextView priceView;
        TextView timeview;
        TextView regionview;
        TextView sellerView;
        TextView description;

        ImageView platformview;
        ImageView pictureView;

        String picture_link;
        String app_name;
        String link;
        String nunstr;
        DecimalFormat decFormat = new DecimalFormat("###,###");

        OnViewHolderItemClickListener onViewHolderItemClickListener;
        LinearLayout linearlayout;

        public ViewHolder(View itemView) {
            super(itemView);

            titleView = itemView.findViewById(R.id.item_title);
            priceView = itemView.findViewById(R.id.item_price);
            timeview = itemView.findViewById(R.id.item_time);
            regionview = itemView.findViewById(R.id.item_reg);
            sellerView = itemView.findViewById(R.id.item_seller);
            platformview = itemView.findViewById(R.id.platform);
            pictureView = itemView.findViewById(R.id.item_picture);

            linearlayout = itemView.findViewById(R.id.linearlayout);
            linearlayout.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    onViewHolderItemClickListener.onViewHolderItemClick();
                }
            });
        }

        public void setItem(PostResponseData item, int position, SparseBooleanArray selectedItems) {
            titleView.setText(item.getTitle());
            String nunstr = decFormat.format(item.getPrice());
            priceView.setText(nunstr+" 원");
            timeview.setText(item.getDate());
            regionview.setText(item.getRegion());
            sellerView.setText(item.getSeller_info());

            app_name = item.getApp_name();
            picture_link = item.getPicture();

            Glide.with(itemView).load(picture_link).into(pictureView);

            switch(app_name){
                case "당근":
                    platformview.setImageResource(R.drawable.ic_karrot_24dp);
                    break;
                case "중고":
                    platformview.setImageResource(R.drawable.ic_joongna_24dp);
                    break;
                case "번개":
                    platformview.setImageResource(R.drawable.ic_ightning_24dp);
                    break;
            }
            changeVisibility(selectedItems.get(position));
        }
        private void changeVisibility(final boolean isExpanded) {
            // ValueAnimator.ofInt(int... values)는 View가 변할 값을 지정, 인자는 int 배열
            ValueAnimator va = isExpanded ? ValueAnimator.ofInt(0, 600) : ValueAnimator.ofInt(600, 0);
            // Animation이 실행되는 시간, n/1000초
            va.setDuration(500);
            va.addUpdateListener(new ValueAnimator.AnimatorUpdateListener() {
                @Override
                public void onAnimationUpdate(ValueAnimator animation) {
                    // imageView의 높이 변경
                    pictureView.getLayoutParams().height = (int) animation.getAnimatedValue();
                    pictureView.requestLayout();
                    // imageView가 실제로 사라지게하는 부분
                    pictureView.setVisibility(isExpanded ? View.VISIBLE : View.GONE);
                }
            });
            // Animation start
            va.start();
        }
        public void setOnViewHolderItemClickListener(OnViewHolderItemClickListener onViewHolderItemClickListener) {
            this.onViewHolderItemClickListener = onViewHolderItemClickListener;
        }

    }
    // 원래 뷰 삭제
    public void clear() {
        this.items.clear();
    }

}
